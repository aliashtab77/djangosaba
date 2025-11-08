from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class SliderModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="نام مکان")
    avatar = models.ImageField(upload_to="slides")
    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلاید ها"
    def __str__(self):
        return self.name


class Information(models.Model):
    travels = models.IntegerField(verbose_name="تعداد سفرها")
    clients = models.IntegerField(verbose_name="تعداد مشتری ها")
    employees = models.IntegerField(verbose_name="تعداد کارمندان")
    countries = models.IntegerField(verbose_name="تعداد کشورها")
    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات"

class PopularDestination(models.Model):
    avatar = models.ImageField(upload_to="special")
    keshvar = models.CharField(max_length=250, verbose_name="نام کشور")
    makan = models.CharField(max_length=250, verbose_name="نام مکان")
    slug = models.ForeignKey(to="BlogModel", on_delete=models.CASCADE, verbose_name="مقاله مرتبط")
    class Meta:
        verbose_name = "مقصد محبوب"
        verbose_name_plural = "مقاصد محبوب"
    def __str__(self):
        return self.makan



class VisaDestination(models.Model):
    avatar = models.ImageField(upload_to="visa")
    keshvar = models.CharField(max_length=250, verbose_name="نام کشور")
    makan = models.CharField(max_length=250, verbose_name="نوع ویزا")
    slug = models.ForeignKey(to="BlogModel", on_delete=models.CASCADE, verbose_name="مقاله مرتبط")
    class Meta:
        verbose_name = "ویزا"
        verbose_name_plural = "ویزا ها"
    def __str__(self):
        return self.makan


class Testimonials(models.Model):
    avatar = models.ImageField(upload_to="testimonials")
    name = models.CharField(max_length=250,verbose_name="نام")
    description = models.CharField(max_length=1000,verbose_name="توضیحات")
    class Meta:
        verbose_name = "توصیفات"
        verbose_name_plural = "توصیفات"
    def __str__(self):
        return self.name



class SpecialModel(models.Model):
    avatar = models.ImageField(upload_to="special")
    keshvar = models.CharField(max_length=250, verbose_name="نام کشور")
    makan = models.CharField(max_length=250, verbose_name="نام مکان")
    price = models.IntegerField(verbose_name="قیمت")
    slug = models.ForeignKey(to="BlogModel", on_delete=models.CASCADE, verbose_name="مقاله مرتبط")
    class Meta:
        verbose_name = "آفر ویژه"
        verbose_name_plural = "آفر های ویژه"

    def __str__(self):
        return self.makan




class MessagesModel(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="نام")
    last_name = models.CharField(max_length=250, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=250, verbose_name="شماره تلفن")
    message = models.TextField(verbose_name="پیام")
    class Meta:
        verbose_name= "پیام کاربر"
        verbose_name_plural= "پیام های کاربران"

    def __str__(self):
        return f"{self.first_name} {self.last_name} phone: {self.phone}"


class HotelModel(models.Model):
    avatar = models.ImageField(upload_to="hotels", verbose_name="عکس هتل")
    name = models.CharField(max_length=255, verbose_name="نام هتل")
    STARS_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    star = models.IntegerField(choices=STARS_CHOICES, default=5, verbose_name="ستاره")
    entekhab = [
        (True, "دارد"),
        (False, "ندارد"),
    ]
    swim = models.BooleanField(choices=entekhab, default=False, verbose_name="استخر شنا")
    gym = models.BooleanField(choices=entekhab, default=False, verbose_name="باشگاه")
    wifi = models.BooleanField(choices=entekhab, default=False, verbose_name="wi-fi")
    roomsevice = models.BooleanField(choices=entekhab, default=False, verbose_name="سرویس اتاق")
    aircondition = models.BooleanField(choices=entekhab, default=False, verbose_name="تهویه هوا")
    resturant = models.BooleanField(choices=entekhab, default=False, verbose_name="رستوران")
    price = models.IntegerField(verbose_name="قیمت برای هر شب")
    class Meta:
        verbose_name = "هتل"
        verbose_name_plural = "هتل ها"
    def __str__(self):
        return self.name

# class WriterModel(models.Model):
#     avatar = models.ImageField(upload_to="writers")
#     name = models.CharField(max_length=255, verbose_name="نام")
#     semat = models.CharField(max_length=255, verbose_name="سمت")
#     description = models.TextField(blank=True, null=True)
#     class Meta:
#         verbose_name = "نویسنده"
#         verbose_name_plural = "نویسندگان"
#     def __str__(self):
#         return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام دسته بندی")
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.name
class BlogModel(models.Model):
    slug = models.SlugField(unique=True,allow_unicode=True,verbose_name="اسلاگ")
    title = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="blogs")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = CKEditor5Field("توضیحات", config_name="extends", null=True)
    short = models.TextField(verbose_name='پیش نمایش',null=True)
    time = models.DateField(auto_now=True)
    # writers = models.ForeignKey(WriterModel, on_delete=models.CASCADE)
    tags = models.TextField(verbose_name="تگ ها(تگ های مورد نظر را با استفاده از کاما از یکدیگر جدا کنید)", null=True, blank=True)
    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
    def __str__(self):
        return self.title

