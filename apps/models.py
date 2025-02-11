from unicodedata import category

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, AbstractUser
from django.db.models import Model, ImageField, ForeignKey, SET_NULL, CASCADE
from django.db.models.fields import CharField, DecimalField, TextField, DateTimeField, SmallIntegerField, EmailField, \
    BooleanField


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = EmailField("email address", unique=True , error_messages={'unique' : 'Bunday email mavjud !'})
    phone_number = CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    objects = CustomUserManager()
    is_active = BooleanField(
        "active",
        default=False,
        help_text="Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts.",
    )


class Category(Model):
    # class Meta:
    #     db_table = 'categories'
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


# class Product(Model):
#     name = CharField(max_length=255)
#     price = DecimalField(max_digits=12 , decimal_places=2)
#     image = ImageField(upload_to='products/')
#     category = ForeignKey('apps.Category' , CASCADE , related_name='products')
#
#     def __str__(self):
#         return self.name

class Order(Model):
    user = ForeignKey('apps.User' ,SET_NULL , null=True , blank=True , related_name="orders")



class Post(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to="posts/")
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

class Todo(Model):
    name = CharField(max_length=255)
    user = ForeignKey('apps.User' , CASCADE , related_name='todos')

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

class Product(Model):
    image = ImageField(upload_to='products/')
    name = CharField(max_length=255)
    size = CharField(max_length=50)
    price = DecimalField(max_digits=9 , decimal_places=2)
    quantity = SmallIntegerField()






