from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/home.html') 

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
    return render(request, 'app/articles/co-so-vat-chat.html')  

def tap_chi(request):
    return render(request, 'app/articles/tap_chi.html') 
