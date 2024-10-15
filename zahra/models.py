from django.db import models

# Create your models here.


class SliderModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام مکان")
    avatar = models.ImageField(upload_to="slides")
    class Meta:
        verbose_name = "اسلاید ها"
    def __str__(self):
        return self.name

class SpecialModel(models.Model):
    avatar = models.ImageField(upload_to="special")
    keshvar = models.CharField(max_length=250, verbose_name="نام کشور")
    makan = models.CharField(max_length=250, verbose_name="نام مکان")
    price = models.IntegerField(verbose_name="قیمت")
    class Meta:
        verbose_name = "آفر های ویژه"

    def __str__(self):
        return self.makan
