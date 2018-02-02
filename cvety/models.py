from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Cvety(models.Model):
    meta = models.CharField("ключевые слова", max_length=70)
    name = models.CharField("название", max_length=50)
    price = models.IntegerField()
    mindescription = models.CharField(" краткое описание", max_length=100)
    description = RichTextUploadingField("описание", blank=True, default='')
    photo = models.ImageField("фото", upload_to="cvety/photos", default="", blank=True)


    class Meta:
        verbose_name = "цветок"
        verbose_name_plural = "цветы"
        ordering = ["id", "name", "price"]

    def __str__(self):
        return self.name

# class FotkaCvetka(models.Model):
#     cvetok = models.ForeignKey(Cvety)
#     photo = models.ImageFIeld(  upload_to="cvety/photos", default="", blank=True)