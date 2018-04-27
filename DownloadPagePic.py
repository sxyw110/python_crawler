#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取百度贴吧图片
import urllib.request
import re
import os, sys

class DownloadPagePic :
    path = '';
    url = "";

    # 根据url获取网页html内容
    def getHtmlContent(self,url):
        page = urllib.request.urlopen(url);
        return page.read()


    # 从html中解析出所有jpg图片的url
    # 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
    def getJPGs(self,html):
        # 解析jpg图片url的正则
        jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)".+?>')  # 注：这里最后加一个'width'是为了提高匹配精确度
        # 解析出jpg的url列表
        try:
            html = html.decode('utf-8')  # python3
            jpgs = re.findall(jpgReg, html)
        except UnicodeDecodeError:
            print("error:url:"+self.url);
            jpgs = [];

        return jpgs

    def mkdirs(self,path):

        if os.path.exists(path):
            pass
        else:
            os.makedirs(path);


    # 用图片url下载图片并保存成制定文件名
    def downloadJPG(self,imgUrl, fileName):

        try:
            urllib.request.urlretrieve(imgUrl, fileName)
        except urllib.error.HTTPError:
            print(imgUrl + ";" + fileName);
        except UnicodeEncodeError:
            print(imgUrl + ";" + fileName);


    # 批量下载图片，默认保存到当前目录下
    def batchDownloadJPGs(self,imgUrls, path='D://crawler//'):
        # 用于给图片命名
        count = 1
        self.mkdirs(path);
        for url in imgUrls:
            self.downloadJPG(url, ''.join([path, '\\{0}.jpg'.format(count)]))
            count = count + 1


    # 封装：从百度贴吧网页下载图片
    def download(self):
        html = self.getHtmlContent(self.url);
        jpgs = self.getJPGs(html);
        self.batchDownloadJPGs(jpgs,self.path)

    def setPath(self,path):
        self.path = path;

    def setUrl(self,url):
        self.url = url;

    def testMethod(self):
        print("aa");

# dp = DownloadPagePic();
# dp.testMethod();
    # def main():
    #     url = 'http://tieba.baidu.com/p/2256306796'
    #     download(url)


if __name__ == '__main__':
    dp = DownloadPagePic();
    os.makedirs('D:\\crawler\\p\\222')