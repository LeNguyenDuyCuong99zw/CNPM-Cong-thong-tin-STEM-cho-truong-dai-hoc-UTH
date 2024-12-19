from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),  # Home page
    path("tong-quan/", views.tong_quan, name='tong_quan'),  
    path("lich-su-hinh-thanh/", views.lich_su_hinh_thanh, name='lich_su_hinh_thanh'),  
    path("su-menh-tam-nhin/", views.su_menh_tam_nhin, name='su_menh_tam_nhin'), 
    path("triet-ly-giao-duc/", views.triet_ly_giao_duc, name='triet_ly_giao_duc'), 
    path("chuc-nang-nhiem-vu/", views.chuc_nang_nhiem_vu, name='chuc_nang_nhiem_vu'),  
    path("co-cau-to-chuc/", views.co_cau_to_chuc, name='co_cau_to_chuc'),  
    path("hoi-dong-truong/", views.hoi_dong_truong, name='hoi_dong_truong'),  
    path("ban-giam-hieu/", views.ban_giam_hieu, name='ban_giam_hieu'), 
    path("co-so-vat-chat/", views.co_so_vat_chat, name='co_so_vat_chat'),  
    path("tap-chi/", views.tap_chi, name='tap_chi'), 
    path("admin/", admin.site.urls),  # Admin URL
]
