from unicodedata import category

from django.db.models import Model, ImageField, ForeignKey, SET_NULL, CASCADE
from django.db.models.fields import CharField, DecimalField, TextField, DateTimeField

class Category(Model):
    # class Meta:
    #     db_table = 'categories'
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):

    name = CharField(max_length=255)
    price = DecimalField(max_digits=12 , decimal_places=2)
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category' , CASCADE , related_name='products')

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

# """
# select name , 10 as num from categories
# """

# """
# User.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count__gt=1)
# """

# async FastApi + async SqlAlchemy
# + Golang

""""""
"""
DJANGO ORM:
    Model.objects.all()
    Model.objects.filter(pk=1).first()
    Model.objects.get(pk=1)
    Model.objects.bulk_create([
        Model(fields=values),
        Model(fields=values),
        Model(fields=values),
        Model(fields=values),
    ])
    Model.objects.annotate(object_name=F("name")).only('object_name')
    Model.objects.all().count()
    obj , is_create = Model.objects.get_or_create(name = "Value")
    select_related    foreign key
    prefetch_related 
        join : N + 1
    
    Model1.objects.filter(model2__field__gte=5).order_by('-model2__id')
    """






