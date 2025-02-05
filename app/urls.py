from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tong-quan/', views.tong_quan, name='tong_quan'),
    path('lich-su-hinh-thanh/', views.lich_su_hinh_thanh, name='lich_su_hinh_thanh'),
    path('su-menh-tam-nhin/', views.su_menh_tam_nhin, name='su_menh_tam_nhin'),
    path('triet-ly-giao-duc/', views.triet_ly_giao_duc, name='triet_ly_giao_duc'),
    path('chuc-nang-nhiem-vu/', views.chuc_nang_nhiem_vu, name='chuc_nang_nhiem_vu'),
    path('co-cau-to-chuc/', views.co_cau_to_chuc, name='co_cau_to_chuc'),
    path('hoi-dong-truong/', views.hoi_dong_truong, name='hoi_dong_truong'),
    path('ban-giam-hieu/', views.ban_giam_hieu, name='ban_giam_hieu'),
    path('co-so-vat-chat/', views.co_so_vat_chat, name='co_so_vat_chat'),
    path('tap-chi/', views.tap_chi, name='tap_chi'),
    path('support/', views.support, name='support'),
    path('tin-tuc-su-kien/', views.news_pages, name='news_pages'),
    path('tin-tuc-su-kien/<slug:slug>/', views.news_detail, name='news_detail'),
    path('thong-bao-moi/', views.announcements, name='announcements'),
    path('thong-bao-moi/<slug:slug>/', views.announcement_detail, name='announcement_detail'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)