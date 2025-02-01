
from django.db.models import Model, ImageField, ForeignKey, SET_NULL, CASCADE
from django.db.models.fields import CharField, DecimalField, TextField, DateTimeField


class Product(Model):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=12 , decimal_places=2)
    image = ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Order(Model):
    user = ForeignKey('auth.User' ,SET_NULL , null=True , blank=True , related_name="orders")



class Post(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to="posts/")
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

class Todo(Model):
    name = CharField(max_length=255)
    user = ForeignKey('auth.User' , CASCADE , related_name='todos')