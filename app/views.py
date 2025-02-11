from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import WebPage, WebPage2tb, Article, CarouselImage
#
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
#khai báo cho phần login 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from .models import TuitionDebt

from django.http import HttpResponse
from django.template import loader
from django.core.cache import cache
from .models import Course
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

#
def home_dashboard(request):
    return render(request, 'app/home_dashboard.html')

def clear_cache(request):
    cache.delete('courses')  # Xóa cache theo key
def courses(request):
  courses = cache.get('courses') # tim kiem data theo key: courses
  if not courses:
      # Nếu không có, tạo dữ liệu và lưu vào cache
      courses = Course.objects.all()
      cache.set('courses', courses, timeout=60*3)  # Lưu cache trong 60 giây
  

  template = loader.get_template('app/course/courses.html')
  context = {
    'courses': courses,
  }
  return HttpResponse(template.render(context, request))



def login_home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Bạn đã đăng nhập!")
			return redirect('login_home')
		else:
			messages.success(request, "Đã xảy ra lỗi khi đăng nhập, vui lòng thử lại...")
			return redirect('login_home')
	else:
		return render(request, 'app/login/login_home.html', {'records':records})



def logout_user(request):
	logout(request)
	messages.success(request, "Bạn đã đăng xuất")
	return redirect('login_home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Bạn đã đăng ký thành công!")
			return redirect('login_home')
	else:
		form = SignUpForm()
		return render(request, 'app/login/register.html', {'form':form})

	return render(request, 'app/login/register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'app_home/login/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Bạn phải đăng nhập để xem trang này!")
		return redirect('login_home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Xóa hồ sơ thành công")
		return redirect('login_home')
	else:
		messages.success(request, "Bạn cần phải đăng nhập")
		return redirect('login_home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Hồ sơ đã được cập nhật")
				return redirect('login_home')
		return render(request, 'app/login/add_record.html', {'form':form})
	else:
		messages.success(request, "Bạn cần phải đăng nhập")
		return redirect('login_home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Hồ sơ đã được cập nhật")
			return redirect('login_home')
		return render(request, 'app/login/update_record.html', {'form':form})
	else:
		messages.success(request, "Bạn cần phải đăng nhập")
		return redirect('login_home')

def support(request):
    return render(request, 'support.html') 

#left-menu

def tuition_debt(request):
    tuition_list = TuitionDebt.objects.all()  # Lấy toàn bộ dữ liệu từ DB
    total_credits = sum(item.credit for item in tuition_list)
    total_tuition = sum(item.tuition_fee for item in tuition_list)

    return render(request, "app/course/tuition_debt.html", {
        "tuition_list": tuition_list,
        "total_credits": total_credits,
        "total_tuition": total_tuition,
    })
