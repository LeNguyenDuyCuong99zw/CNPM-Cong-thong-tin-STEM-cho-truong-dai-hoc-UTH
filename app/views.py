from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import WebPage, WebPage2tb, Article, CarouselImage, CustomUser, SupportRequest, ChatMessage, Record, TuitionDebt, Course
from .forms import CustomLoginForm, SignUpForm, AddRecordForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.core.cache import cache
from django.utils import timezone

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
    return render(request, 'app/support/support.html')

def supportuser(request):
    hovaten = request.session.get('hovaten', 'Guest')
    return render(request, 'app/support/supportuser.html', {'hovaten': hovaten})

def admin_support_requests(request):
    requests = SupportRequest.objects.all()
    return render(request, 'app/support/admin_support_requests.html', {'requests': requests})

def respond(request, request_id):
    support_request = get_object_or_404(SupportRequest, id=request_id)
    if request.method == 'POST':
        response = request.POST.get('response')
        support_request.response = response
        support_request.response_date = timezone.now()
        support_request.status = 'closed'
        support_request.save()
        return redirect('admin_support_requests')
    return render(request, 'app/respond.html', {'support_request': support_request})

def login(request):
    return render(request, 'app/login.html')

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

def news_tuyen(request):
    news_list = WebPage.objects.filter(category='tuyen-sinh').order_by('-created_at')
    paginator = Paginator(news_list, 10)  # Hiển thị 10 tin tức mỗi trang

    page_number = request.GET.get('page')
    news_pages = paginator.get_page(page_number)
    
    return render(request, 'app/news_tuyen.html', {'news_pages': news_pages})

def news_tuyendetal(request, slug):
    page = get_object_or_404(WebPage, slug=slug)
    related_pages = WebPage.objects.filter(category=page.category).exclude(id=page.id).order_by('-created_at')[:5]
    return render(request, 'app/news_tuyendetal.html', {'page': page, 'related_pages': related_pages})

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

# View xử lý đăng nhập tùy chỉnh
def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = CustomUser.objects.get(username=username, password=password)
                # Lưu thông tin người dùng vào session
                request.session['hovaten'] = user.hovaten
                # Chuyển hướng đến trang supportuser
                return redirect('supportuser')
            except CustomUser.DoesNotExist:
                form.add_error(None, 'Tên đăng nhập hoặc mật khẩu không đúng')
    else:
        form = CustomLoginForm()
    return render(request, 'app/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

# View xử lý yêu cầu hỗ trợ
def handle_support_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = request.POST['user']
        topic = request.POST['topic']
        request_title = request.POST['request-title']
        request_content = request.POST['request-content']
        attachment = request.FILES.get('attachment')

        support_request = SupportRequest(
            email=email,
            user=user,
            topic=topic,
            request_title=request_title,
            request_content=request_content,
            attachment=attachment,
            status='open'
        )
        support_request.save()

        return redirect('supportuser')
    return HttpResponse("Invalid request method", status=405)

# View hiển thị yêu cầu hỗ trợ của người dùng đã đăng nhập
@login_required
def user_support_requests(request):
    hovaten = request.session.get('hovaten', None)
    if hovaten:
        requests = SupportRequest.objects.filter(user=hovaten)
        open_requests_count = requests.filter(status='open').count()
        closed_requests_count = requests.filter(status='closed').count()
        return render(request, 'app/support/user_support_requests.html', {
            'requests': requests,
            'hovaten': hovaten,
            'open_requests_count': open_requests_count,
            'closed_requests_count': closed_requests_count
        })
    else:
        return redirect('login')

# View hiển thị chi tiết yêu cầu hỗ trợ
@login_required
def support_request_detail(request, request_id):
    support_request = get_object_or_404(SupportRequest, id=request_id)
    hovaten = request.session.get('hovaten', None)
    if request.method == 'POST':
        sender = request.POST['sender']
        message = request.POST['message']
        chat_message = ChatMessage(
            support_request=support_request,
            sender=sender,
            message=message
        )
        chat_message.save()
        return redirect('support_request_detail', request_id=request_id)
    return render(request, 'app/support/support_request_detail.html', {
        'support_request': support_request,
        'hovaten': hovaten
    })

# View xử lý gửi tin nhắn từ trang admin_support_requests
def send_message(request, request_id):
    support_request = get_object_or_404(SupportRequest, id=request_id)
    if request.method == 'POST':
        sender = request.POST['sender']
        message = request.POST['message']
        chat_message = ChatMessage(
            support_request=support_request,
            sender=sender,
            message=message,
            timestamp=timezone.now()
        )
        chat_message.save()
        return redirect('admin_support_requests')
    return redirect('admin_support_requests')

# View hiển thị chi tiết yêu cầu hỗ trợ từ trang admin
def view_details(request, request_id):
    support_request = get_object_or_404(SupportRequest, id=request_id)
    return render(request, 'app/support/view_details.html', {'request': support_request})

# Các view mới thêm vào
def home_dashboard(request):
    return render(request, 'app/home_dashboard.html')

def clear_cache(request):
    cache.delete('courses')  # Xóa cache theo key

def courses(request):
    courses = cache.get('courses')  # Tìm kiếm data theo key: courses
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
        return render(request, 'app/login/login_home.html', {'records': records})

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
        return render(request, 'app/login/register.html', {'form': form})

    return render(request, 'app/login/register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'app/login/record.html', {'customer_record': customer_record})
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
        return render(request, 'app/login/add_record.html', {'form': form})
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
        return render(request, 'app/login/update_record.html', {'form': form})
    else:
        messages.success(request, "Bạn cần phải đăng nhập")
        return redirect('login_home')

def tuition_debt(request):
    tuition_list = TuitionDebt.objects.all()  # Lấy toàn bộ dữ liệu từ DB
    total_credits = sum(item.credit for item in tuition_list)
    total_tuition = sum(item.tuition_fee for item in tuition_list)

    return render(request, "app/course/tuition_debt.html", {
        "tuition_list": tuition_list,
        "total_credits": total_credits,
        "total_tuition": total_tuition,
    })