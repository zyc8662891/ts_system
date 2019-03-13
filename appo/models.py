from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    usr = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    entry_time = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish_date = models.DateField()
    publish = models.ForeignKey(to='Publish', on_delete=models.SET_NULL, null=True, db_constraint=False)
    # 自动建立第三张表
    author = models.ManyToManyField(to='Author', db_constraint=False)


# id name address
class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=20)



# id name author_detail
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.SET_NULL, null=True, db_constraint=False)


# id age telephone info
class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    telephone = models.BigIntegerField()
    info = models.CharField(max_length=60)










