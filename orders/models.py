from django.db import models
from cvety.models import Cvety
# Create your models here.
class Order(models.Model):
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=20)
    date = models.DateField("дата", auto_now_add=True)


