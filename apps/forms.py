import re

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.forms import Form, ImageField, CharField, DecimalField, IntegerField, EmailField
from django.forms.models import ModelForm

from apps.models import Todo, Product, User
from redis import Redis

redis = Redis(decode_responses=True)

class TodoModelForm(ModelForm):
    class Meta:
        model = Todo
        fields = "name",


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        l = len(name)
        if l < 4:
            raise ValidationError("Maxsulot nomining uzunligi 4 dan kichik bo'lmasin")
        if l > 255:
            raise ValidationError("Maxsulot nomining uzunligi 255 dan oshib ketmasin")
        name = name.upper()
        return name


class ProductForm(Form):
    image = ImageField()
    name = CharField()
    size = CharField()
    price = DecimalField()
    quantity = IntegerField(min_value=1, error_messages={'min_value':"Sanog'i 1 dan kam bo'lishi mumkin emas"})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        l = len(name)
        if l < 4:
            raise ValidationError("Maxsulot nomining uzunligi 4 dan kichik bo'lmasin")
        if l > 255:
            raise ValidationError("Maxsulot nomining uzunligi 255 dan oshib ketmasin")
        name = name.upper()
        return name


    def save(self):
        Product.objects.create(**self.cleaned_data)


class RegisterModelForm(ModelForm):
    class Meta:
        model = User
        fields = 'phone_number' , 'email' , 'password'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise ValidationError("Password uzunligi 4 ta belgidan kam bo'lmasin")
        return make_password(password)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise ValidationError("Emailda xatolik bor !")
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        pattern = r"^\+998(?:33|55|77|88|90|91|93|94|95|97|98|99)\d{7}$"
        if not re.match(pattern, phone):
            raise ValidationError("Telefon raqamda xatolik bor ")
        return phone


class VerifyForm(Form):
    code = IntegerField()


    def update(self , email):
        User.objects.filter(email = email).update(is_active=True)












# Category form:
#     name(max_length=10 , min_length=3)


"""
1) Template 
2) view
3) url
4) model form 
5) save
"""


