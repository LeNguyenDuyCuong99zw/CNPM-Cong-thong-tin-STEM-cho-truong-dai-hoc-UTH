from django.db import models
from django.contrib.sites.models import Site
from django.utils.text import slugify
import re
from django.utils import timezone

class WebPage(models.Model):
    CATEGORY_CHOICES = [
        ('tin-tuc-su-kien', 'Tin Tức'),
        ('other', 'Khác'),
    ]

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='app/images/tintuc/', blank=True, null=True)
    content = models.TextField(null=True, blank=True)  
    video_url = models.URLField(null=True, blank=True)
    image2 = models.ImageField(upload_to='app/images/tintuc/', blank=True, null=True)  # Thêm trường image2
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_embed_url(self):
        if self.video_url:
            youtube_id = re.search(r'v=([^&]+)', self.video_url)
            if youtube_id:
                return f"https://www.youtube.com/embed/{youtube_id.group(1)}"
        return None

    def __str__(self):
        return self.name

class WebPage2tb(models.Model):
    CATEGORY_CHOICES = [
        ('thong-bao-moi', 'Thông Báo'),
        ('other', 'Khác'),
    ]

    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='app/images/tintuc/', blank=True, null=True)
    content = models.TextField(null=True, blank=True)  
    video_url = models.URLField(null=True, blank=True)
    image2 = models.ImageField(upload_to='app/images/tintuc/', blank=True, null=True)  # Thêm trường image2
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_embed_url(self):
        if self.video_url:
            youtube_id = re.search(r'v=([^&]+)', self.video_url)
            if youtube_id:
                return f"https://www.youtube.com/embed/{youtube_id.group(1)}"
        return None

    def __str__(self):
        return self.name

class Content(models.Model):
    webpage = models.ForeignKey(WebPage, related_name='contents', on_delete=models.CASCADE, null=True, blank=True)
    webpage2tb = models.ForeignKey(WebPage2tb, related_name='contents', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)  # Thêm trường order

    class Meta:
        ordering = ['order']  # Sắp xếp theo trường order

    def __str__(self):
        return self.text[:50]
    
class Content2(models.Model):
    webpage = models.ForeignKey(WebPage, related_name='contents2', on_delete=models.CASCADE, null=True, blank=True)
    webpage2tb = models.ForeignKey(WebPage2tb, related_name='contents2', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)  # Thêm trường order

    class Meta:
        ordering = ['order']  # Sắp xếp theo trường order

    def __str__(self):
        return self.text[:50]
    
class Image(models.Model):
    webpage = models.ForeignKey(WebPage, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    webpage2tb = models.ForeignKey(WebPage2tb, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='app/images/tintuc/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # Thêm trường order

    class Meta:
        ordering = ['order']  # Sắp xếp theo trường order

    def __str__(self):
        return self.image.url

class Image2(models.Model):
    webpage = models.ForeignKey(WebPage, related_name='images2', on_delete=models.CASCADE, null=True, blank=True)
    webpage2tb = models.ForeignKey(WebPage2tb, related_name='images2', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='app/images/tintuc/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # Thêm trường order

    class Meta:
        ordering = ['order']  # Sắp xếp theo trường order

    def __str__(self):
        return self.image.url

class Content3(models.Model):
    webpage = models.ForeignKey(WebPage, related_name='contents3', on_delete=models.CASCADE, null=True, blank=True)
    webpage2tb = models.ForeignKey(WebPage2tb, related_name='contents3', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)  # Thêm trường order

    class Meta:
        ordering = ['order']  # Sắp xếp theo trường order

    def __str__(self):
        return self.text[:50]

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text
#login dashboard
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	school =  models.CharField(max_length=50)
	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

#
class TuitionDebt(models.Model):
    semester = models.CharField(max_length=255)  
    class_code = models.CharField(max_length=50) 
    subject_name = models.CharField(max_length=255)  
    credit = models.IntegerField()  
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2) 
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    registration_status = models.CharField(max_length=100, default="Đăng ký mới")  
    payment_date = models.DateField(null=True, blank=True)  
    deduction_plus = models.DecimalField(max_digits=10, decimal_places=2, default=0)  
    deduction_minus = models.DecimalField(max_digits=10, decimal_places=2, default=0)  

    def __str__(self):
        return self.subject_name
