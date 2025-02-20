from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, WebPage, Content, Content2, Content3, Image , StudentRegistration

class WebPageForm(forms.ModelForm):
    class Meta:
        model = WebPage
        fields = ['site', 'name', 'category', 'slug', 'image', 'content', 'video_url', 'image2', 'created_at']
        labels = {
            'site': 'Trang web',
            'name': 'Tên',
            'category': 'Danh mục',
            'slug': 'Slug',
            'image': 'Hình ảnh',
            'content': 'Nội dung',
            'video_url': 'URL video',
            'image2': 'Hình ảnh 2',
            'created_at': 'Ngày tạo',
        }
        widgets = {
            'site': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text', 'order']
        labels = {
            'text': 'Nội dung',
            'order': 'Thứ tự',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Content2Form(forms.ModelForm):
    class Meta:
        model = Content2
        fields = ['text', 'order']
        labels = {
            'text': 'Nội dung',
            'order': 'Thứ tự',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Content3Form(forms.ModelForm):
    class Meta:
        model = Content3
        fields = ['text', 'order']
        labels = {
            'text': 'Nội dung',
            'order': 'Thứ tự',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class StudentNewForm(forms.Form):
    code = forms.CharField(label="code", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseNewForm(forms.Form):
    name = forms.CharField(label="name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(label="year", min_value=1995, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    startDate = forms.DateField(label="startDate", widget=forms.DateInput(attrs={'class': 'form-control'}))
    endDate = forms.DateField(label="endDate", widget=forms.DateInput(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label="active", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    school = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"School", "class":"form-control"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)

# Custom Login Form
class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Tên đăng nhập', 'class': 'form-control'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu', 'class': 'form-control'}), required=True)

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name', 'phone', 'dob', 'email', 'school', 'location', 'facebook']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ và tên'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Nhập ngày sinh'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập trường học'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chọn tỉnh / thành phố'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Nhập URL Facebook'}),
        }
        error_messages = {
            'name': {
                'required': 'Vui lòng nhập họ và tên.',
            },
            'phone': {
                'required': 'Vui lòng nhập số điện thoại.',
            },
            'dob': {
                'required': 'Vui lòng nhập ngày sinh.',
            },
            'email': {
                'required': 'Vui lòng nhập email.',
            },
            'school': {
                'required': 'Vui lòng nhập trường học.',
            },
            'location': {
                'required': 'Vui lòng chọn tỉnh / thành phố.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Họ và tên"
        self.fields['phone'].label = "Số điện thoại"
        self.fields['dob'].label = "Ngày sinh"
        self.fields['email'].label = "Email"
        self.fields['school'].label = "Trường học"
        self.fields['location'].label = "Tỉnh / Thành phố"
        self.fields['facebook'].label = "Facebook"

        for field in self.fields.values():
            field.required = False  # Disable the required attribute
            field.error_messages = {'required': 'Vui lòng điền thông tin này.'}
            
class StudentLoginForm(forms.Form):
    name = forms.CharField(
        label="Họ và tên",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ và tên'})
    )
    phone = forms.CharField(
        label="Số điện thoại",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'})
    )

    def __init__(self, *args, **kwargs):
        super(StudentLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True  # Make the fields required
            field.error_messages = {'required': 'Vui lòng điền thông tin này.'}