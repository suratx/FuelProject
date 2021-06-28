from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
# https://www.youtube.com/watch?v=UxTwFMZ4r5k

class Client(models.Model):

# Django does not know the Field type of Client , because the object is not defined in Django
# special way of being removed (foreignkey)
# after writing MODELS, we actually tell Django we write Terminal 'python manage.py makemigrations fuel_app'
# and then terminal , 'python manage.py migrate'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    # email = models.EmailField()
    zipcode = models.CharField(max_length=5)

class Quote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    address = models.CharField(max_length=100)
    gallons = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)