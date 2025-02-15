from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddNewsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_add_news(self):
        # Giả sử bạn đã đăng nhập thành công trước đó
        self.browser.get('http://127.0.0.1:8000/admin/app/webpage/add/')

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )

        site_input = self.browser.find_element(By.NAME, 'site')
        name_input = self.browser.find_element(By.NAME, 'name')
        category_input = self.browser.find_element(By.NAME, 'category')
        content_input = self.browser.find_element(By.NAME, 'content')

        site_input.send_keys('Example')
        name_input.send_keys('UTH tiên phong trong đào tạo nguồn nhân lực cho Dự án đường sắt tốc độ cao Bắc - Nam')
        category_input.send_keys('tin-tuc-su-kien')
        content_input.send_keys('Nội dung của tin tức mới.')

        self.browser.find_element(By.NAME, '_save').click()

        # Kiểm tra xem mục tin tức đã được lưu thành công hay chưa
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'success'))
        )
        self.assertIn('was added successfully', self.browser.page_source)