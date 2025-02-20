from django.db import models
from django.contrib.sites.models import Site
from django.utils.text import slugify
import re
from django.utils import timezone

class WebPage(models.Model):
    CATEGORY_CHOICES = [
        ('tin-tuc-su-kien', 'Tin Tức'),
        ('tuyen-sinh', 'Tuyển Sinh'),
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

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    hovaten = models.CharField(max_length=255, default='Default Name')  # Thêm trường hovaten với giá trị mặc định
    email = models.EmailField(unique=True, default='example@example.com')  # Thêm trường email với giá trị mặc định

    def __str__(self):
        return self.username

class SupportRequest(models.Model):
    email = models.EmailField(max_length=120)
    user = models.CharField(max_length=80)
    topic = models.CharField(max_length=120)
    request_title = models.CharField(max_length=200)
    request_content = models.TextField()
    attachment = models.FileField(upload_to='uploads/', null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Thêm trường created_at
    response_date = models.DateTimeField(null=True, blank=True)  # Thêm trường response_date
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')  # Thêm trường status

    def __str__(self):
        return self.request_title

class ChatMessage(models.Model):
    support_request = models.ForeignKey(SupportRequest, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=80)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.message[:50]}'

# login dashboard
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    school = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# left-menu
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

# Thêm lớp Course
class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Report(models.Model):
    report_date = models.DateField(auto_now_add=True)
    total_webpages = models.IntegerField(default=0)
    total_webpages2tb = models.IntegerField(default=0)
    total_support_requests = models.IntegerField(default=0)
    total_articles = models.IntegerField(default=0)

    def generate_report(self):
        self.total_webpages = WebPage.objects.count()
        self.total_webpages2tb = WebPage2tb.objects.count()
        self.total_support_requests = SupportRequest.objects.count()
        self.total_articles = Article.objects.count()
        self.save()

    def __str__(self):
        return f"Report for {self.report_date}"

class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)  # Make dob optional
    email = models.EmailField()
    school = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name