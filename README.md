Để chạy và khởi động project django web Cổng thông stem cho trường đại học UTH ta cần phải thực hiện các bước sau :

tải django : pip install django 
update django pip install --upgrade Django

tải các thư viện trong requirements trong terminal :pip install -r requirements.txt
bật Docker trên máy và dùng lệnh : docker compose up

Chạy PROJECT
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
