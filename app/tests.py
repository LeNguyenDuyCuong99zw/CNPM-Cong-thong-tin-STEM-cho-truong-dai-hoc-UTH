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
        # Directly access the admin page for adding news
        self.browser.get('http://127.0.0.1:8000/admin/app/webpage/add/')

        # Wait for the login form to be present
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        # Fill in the login form
        username_input = self.browser.find_element(By.NAME, 'username')
        password_input = self.browser.find_element(By.NAME, 'password')
        username_input.send_keys('DuyCuong')
        time.sleep(2)  # Delay for 2 seconds
        password_input.send_keys('1234')
        time.sleep(2)  # Delay for 2 seconds
        password_input.send_keys(Keys.RETURN)

        # Wait for the admin page to load after login
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )

        site_input = self.browser.find_element(By.NAME, 'site')
        name_input = self.browser.find_element(By.NAME, 'name')
        category_input = self.browser.find_element(By.NAME, 'category')
        content_input = self.browser.find_element(By.NAME, 'content')

        site_input.send_keys('Example')
        time.sleep(2)  # Delay for 2 seconds
        name_input.send_keys('UTH tiên phong trong đào tạo nguồn nhân lực cho Dự án đường sắt tốc độ cao Bắc - Nam')
        time.sleep(2)  # Delay for 2 seconds
        category_input.send_keys('tin-tuc-su-kien')
        time.sleep(2)  # Delay for 2 seconds
        content_input.send_keys('Nội dung của tin tức mới.')
        time.sleep(2)  # Delay for 2 seconds

        self.browser.find_element(By.NAME, '_save').click()

        # Delay for 10 seconds
        time.sleep(10)

        # Kiểm tra xem mục tin tức đã được lưu thành công hay chưa
        self.assertIn('was added successfully', self.browser.page_source)

        # Navigate to the next page to add more content
        self.browser.get('http://127.0.0.1:8000/admin/app/webpage2tb/add/')

        # Wait for the form to be present
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )

        # Fill in the form on the new page
        site_input = self.browser.find_element(By.NAME, 'site')
        name_input = self.browser.find_element(By.NAME, 'name')
        category_input = self.browser.find_element(By.NAME, 'category')
        content_input = self.browser.find_element(By.NAME, 'content')

        site_input.send_keys('Example2')
        time.sleep(2)  # Delay for 2 seconds
        name_input.send_keys('Another news title')
        time.sleep(2)  # Delay for 2 seconds
        category_input.send_keys('thong-bao-moi')
        time.sleep(2)  # Delay for 2 seconds
        content_input.send_keys('Content of another news.')
        time.sleep(2)  # Delay for 2 seconds

        self.browser.find_element(By.NAME, '_save').click()

        # Delay for 10 seconds
        time.sleep(10)

        # Kiểm tra xem mục tin tức đã được lưu thành công hay chưa
        self.assertIn('was added successfully', self.browser.page_source)