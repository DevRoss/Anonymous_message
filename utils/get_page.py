from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
from Anonymous_message.settings import PAGE_SHOT_ROOT, PAGE_SHOT_URL
import hashlib

if not os.path.exists(PAGE_SHOT_ROOT):
    os.mkdir(PAGE_SHOT_ROOT)


class Browser:
    driver = webdriver.PhantomJS()

    def get_page(self, url):
        self.driver.get(url)

    def get_full_page_shot(self, url):
        self.get_page(url)
        total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        size = self.driver.get_window_size()
        print(size['width'], size['height'])
        y = 0
        # 滚动到最后
        while y < total_height:
            self.driver.execute_script("window.scrollBy({width}, {height})".format(width=0, height=size['height']))
            time.sleep(0.5)
            y += size['height']
            print(y)
            total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        # sha1 计算重复
        sha1 = hashlib.sha1(self.driver.title.encode()).hexdigest()
        file_path = os.path.join(PAGE_SHOT_ROOT, sha1 + '.png')
        self.driver.save_screenshot(file_path)
        self.close()
        return os.path.join(PAGE_SHOT_URL, sha1 + '.png')

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    browser = Browser()
    # url = 'http://www.bilibili.com/'
    url = 'http://www.dilidili.wang/'
    browser.get_full_page_shot(url)
