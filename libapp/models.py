from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book_Signup(models.Model):
    book_user=models.CharField(max_length=50)
    book_password = models.CharField(max_length=50)
    def __str__(self):
        return self.book_user


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
   

class Book_Store(models.Model):
    book_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    publish_date = models.CharField(max_length=20)
    book_price = models.IntegerField()
    numbers = models.IntegerField()
    book_image = models.ImageField(upload_to='book_images/')
    def __str__(self):
        return self.book_name
    

class Order(models.Model):
    o_user = models.CharField(max_length=50)
    book =  models.ForeignKey(Book_Store, on_delete=models.CASCADE)
    payment_method =models.CharField(max_length=25, null=True)
    order_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20)
    def __str__(self):

        return self.o_user
    

class Cart(models.Model):
    book = models.ForeignKey(Book_Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book.book_name



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_image = models.ImageField(upload_to='wishlist_images/')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

