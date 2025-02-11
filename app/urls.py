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
    path('support/request/<int:request_id>/', views.view_details, name='view_details'),
    path('supportuser/', views.supportuser, name='supportuser'),
    path('send_message/<int:request_id>/', views.send_message, name='send_message'),
    path('login/', views.login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('handle_support_request/', views.handle_support_request, name='handle_support_request'),
    path('admin_support_requests/', views.admin_support_requests, name='admin_support_requests'),
    path('user_support_requests/', views.user_support_requests, name='user_support_requests'),
    path('support_request_detail/<int:request_id>/', views.support_request_detail, name='support_request_detail'),
    path('respond/<int:request_id>/', views.respond, name='respond'),
    path('tin-tuc-su-kien/', views.news_pages, name='news_pages'),
    path('tin-tuc-su-kien/<slug:slug>/', views.news_detail, name='news_detail'),
    path('tuyen-sinh/', views.news_tuyen, name='news_tuyen'),
    path('tuyen-sinh/<slug:slug>/', views.news_tuyendetal, name='news_tuyendetal'),
    path('thong-bao-moi/', views.announcements, name='announcements'),
    path('thong-bao-moi/<slug:slug>/', views.announcement_detail, name='announcement_detail'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('custom-login/', views.custom_login, name='custom_login'),  # Thêm đường dẫn cho view đăng nhập tùy chỉnh
    # Khai báo phần login
    path('login_home/', views.login_home, name='login_home'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
    path('home_dashboard/', views.home_dashboard, name='home_dashboard'),
    # left-menu
    path('tuition_debt/', views.tuition_debt, name='tuition_debt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)