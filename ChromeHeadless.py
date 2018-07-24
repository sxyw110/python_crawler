#-*-coding:utf-8-*-
import urllib

import io
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from MysqlUtils import MysqlUtils


class ChromeHeadless:
    # 用图片url下载图片并保存成制定文件名
    def downloadJPG(self, imgUrl, fileName):

        try:
            urllib.request.urlretrieve(imgUrl, fileName)
        except urllib.error.HTTPError:
            print(imgUrl + ";" + fileName);
        except UnicodeEncodeError:
            print(imgUrl + ";" + fileName);

    def getPagePreUrl(self,url):
        self.getDriver(url);




    def getPageContent(self,url):
        driver = self.getDriver();

        MysqlUtils.initDB();

        while True:
            driver.get(url);
            self.savePageUrl(driver);

            try:
                preElement = driver.find_element_by_class_name("previous-comment-page");
                url = preElement.get_attribute("href");
                print("next url:"+ url);
            except NoSuchElementException:
                break;

        driver.close();
        MysqlUtils.closeDB();


    def savePageUrl(self,driver):
        elements = driver.find_elements_by_class_name("view_img_link");
        for element in elements:
            url = element.get_attribute("href");
            print("start dowload:"+ url);
            file = urllib.request.urlopen(url)
            tmpIm = io.BytesIO(file.read())
            print("end dowload:"+ url);
            im = Image.open(tmpIm)


            MysqlUtils.inserUrl(url,im.width,im.height);
            print(element.get_attribute("href"));
        #保存到数据库




    def getDriver(self):
        options = webdriver.ChromeOptions();
        options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",--headless');
        options.add_argument('--headless');
        options.add_argument('--disable-gpu');
        driver = webdriver.Chrome(chrome_options=options);
        return driver;

if __name__ == '__main__':
    url = "http://jandan.net/ooxx"
    # url = "https://www.baidu.com";
    ch = ChromeHeadless();
    # driver = ch.getDriver();
    ch.getPageContent(url);
    # options = webdriver.ChromeOptions()
    # url = "http://www.baidu.com"
    # options.add_argument(
    #     'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",--headless');
    # # options.add_argument('--headless')
    # # options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=options)

    # elements  = driver.find_elements_by_class_name("view_img_link");
    # for element in elements:
    #     print(element.get_attribute("href"));
    # time.sleep(3);
    # print(driver.page_source);
    # preElement = driver.find_element_by_class_name("previous-comment-page");
    # print(preElement.get_attribute("href"));
    # html = driver.page_source;
