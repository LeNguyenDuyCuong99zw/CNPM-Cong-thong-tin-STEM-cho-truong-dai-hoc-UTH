# Sử dụng image chính thức của Python
FROM python:3.11

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file yêu cầu vào container
COPY requirements.txt /app/

# Cài đặt các gói yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . /app/

# Chạy lệnh migrate và collectstatic
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Chạy server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]