from django.contrib import admin
from django.utils.html import format_html
from .models import WebPage, WebPage2tb, Content, Content2, Image, Image2, Content3, Article, CarouselImage, CustomUser, SupportRequest, ChatMessage, Report, StudentRegistration

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1
    fields = ('text', 'order',)  # Thêm trường order

class Content2Inline(admin.TabularInline):
    model = Content2
    extra = 1
    fields = ('text', 'order',)  # Thêm trường order

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'caption', 'order',)  # Thêm trường order

class Image2Inline(admin.TabularInline):
    model = Image2
    extra = 1
    fields = ('image', 'caption', 'order',)  # Thêm trường order

class Content3Inline(admin.TabularInline):
    model = Content3
    extra = 1
    fields = ('text', 'order',)  # Thêm trường order

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1
    fields = ('sender', 'message', 'timestamp',)  # Thêm trường timestamp

@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'category', 'created_at', 'image_tag', 'video_link', 'formatted_content', 'formatted_content2', 'formatted_content3', 'image2_tag')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ContentInline, Content2Inline, ImageInline, Image2Inline, Content3Inline]
    ordering = ['-created_at']  # Sắp xếp theo created_at giảm dần

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Image'

    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />'.format(obj.image2.url))
        return "-"
    image2_tag.short_description = 'Image2'

    def video_link(self, obj):
        if obj.video_url:
            return format_html('<a href="{}" target="_blank">Video</a>'.format(obj.video_url))
        return "-"
    video_link.short_description = 'Video'

    def formatted_content(self, obj):
        contents = obj.contents.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content.short_description = 'Content'

    def formatted_content2(self, obj):
        contents = obj.contents2.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content2.short_description = 'Content2'

    def formatted_content3(self, obj):
        contents = obj.contents3.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content3.short_description = 'Content3'

@admin.register(WebPage2tb)
class WebPage2tbAdmin(admin.ModelAdmin):
    list_display = ('name', 'site', 'category', 'created_at', 'image_tag', 'video_link', 'formatted_content', 'formatted_content2', 'formatted_content3', 'image2_tag')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ContentInline, Content2Inline, ImageInline, Image2Inline, Content3Inline]
    ordering = ['-created_at']  # Sắp xếp theo created_at giảm dần

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Image'

    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />'.format(obj.image2.url))
        return "-"
    image2_tag.short_description = 'Image2'

    def video_link(self, obj):
        if obj.video_url:
            return format_html('<a href="{}" target="_blank">Video</a>'.format(obj.video_url))
        return "-"
    video_link.short_description = 'Video'

    def formatted_content(self, obj):
        contents = obj.contents.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content.short_description = 'Content'

    def formatted_content2(self, obj):
        contents = obj.contents2.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content2.short_description = 'Content2'

    def formatted_content3(self, obj):
        contents = obj.contents3.all()
        html_content = ''.join([format_html('<p>{}</p>', content.text) for content in contents])
        return format_html('<div>{}</div>', html_content)
    formatted_content3.short_description = 'Content3'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')
    search_fields = ('alt_text',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'hovaten', 'email')
    search_fields = ('username', 'hovaten', 'email')

@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'topic', 'request_title', 'created_at', 'response_date', 'status')
    search_fields = ('email', 'user', 'topic', 'request_title')
    ordering = ['-created_at']
    inlines = [ChatMessageInline]

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'total_webpages', 'total_webpages2tb', 'total_support_requests', 'total_articles')
    readonly_fields = ('report_date', 'total_webpages', 'total_webpages2tb', 'total_support_requests', 'total_articles')
    ordering = ['-report_date']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'dob', 'email', 'school', 'location', 'facebook')
    search_fields = ('name', 'phone', 'email', 'school', 'location')
    ordering = ['-dob']  # Order by date of birth descending