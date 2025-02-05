from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import WebPage, WebPage2tb, Article, CarouselImage

# Các view hiện có
def home(request):
    news_pages = WebPage.objects.filter(category='tin-tuc-su-kien').order_by('-created_at')[:5]
    announcements = WebPage2tb.objects.filter(category='thong-bao-moi').order_by('-created_at')[:5]
    carousel_images = CarouselImage.objects.all()[:5]  
    return render(request, 'app/home.html', {'news_pages': news_pages, 'announcements': announcements, 'carousel_images': carousel_images})

def tong_quan(request):
    return render(request, 'app/articles/tong_quan.html')

def lich_su_hinh_thanh(request):
    return render(request, 'app/articles/lich_su_hinh_thanh.html')

def su_menh_tam_nhin(request):
    return render(request, 'app/articles/su_menh_tam_nhin.html')

def triet_ly_giao_duc(request):
    return render(request, 'app/articles/triet_ly_giao_duc.html')

def chuc_nang_nhiem_vu(request):
    return render(request, 'app/articles/chuc_nang_nhiem_vu.html')

def co_cau_to_chuc(request):
    return render(request, 'app/articles/co-cau-to-chuc.html')

def hoi_dong_truong(request):
    return render(request, 'app/articles/hoi_dong_truong.html')

def ban_giam_hieu(request):
    return render(request, 'app/articles/ban-giam-hieu.html')

def co_so_vat_chat(request):
    return render(request, 'app/articles/co_so_vat_chat.html')

def tap_chi(request):
    return render(request, 'app/articles/tap_chi.html')

def support(request):
    return render(request, 'app/support.html')

# Các view mới
def news_pages(request):
    news_list = WebPage.objects.filter(category='tin-tuc-su-kien').order_by('-created_at')
    paginator = Paginator(news_list, 10)  # Hiển thị 10 tin tức mỗi trang

    page_number = request.GET.get('page')
    news_pages = paginator.get_page(page_number)
    
    return render(request, 'app/news_pages.html', {'news_pages': news_pages})

def news_detail(request, slug):
    page = get_object_or_404(WebPage, slug=slug)
    related_pages = WebPage.objects.filter(category=page.category).exclude(id=page.id).order_by('-created_at')[:5]
    return render(request, 'app/news_detail.html', {'page': page, 'related_pages': related_pages})

# Các view cho WebPage2tb
def announcements(request):
    announcement_list = WebPage2tb.objects.filter(category='thong-bao-moi').order_by('-created_at')
    paginator = Paginator(announcement_list, 10)  # Hiển thị 10 thông báo mỗi trang

    page_number = request.GET.get('page')
    announcements = paginator.get_page(page_number)
    
    return render(request, 'app/announcements.html', {'announcements': announcements})

def announcement_detail(request, slug):
    page = get_object_or_404(WebPage2tb, slug=slug)
    related_pages = WebPage2tb.objects.filter(category=page.category).exclude(id=page.id).order_by('-created_at')[:5]
    return render(request, 'app/announcement_detail.html', {'page': page, 'related_pages': related_pages})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'app/article_detail.html', {'article': article})