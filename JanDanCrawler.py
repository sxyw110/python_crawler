#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取图片
import urllib.request
import re
import os, sys
from bs4 import BeautifulSoup
import hashlib
import base64

class JanDanCrawler:
    path = '';
    url = "";

    # 根据url获取网页html内容
    def getHtmlContent(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        page = urllib.request.urlopen(req);
        return page.read()



    # 从html中解析出所有jpg图片的url
    # 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
    def getJPGsByBS(self, html):
        soup = BeautifulSoup(html, "html.parser");
        print(soup);
        imgs = soup.find_all('a',class_="view_img_link");
        
        jpgs =[];
        for img in imgs:
            jpgs.append(img.get('href'));

        print(jpgs);
        print( len(jpgs));
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
            self.downloadJPG(url, ''.join([path, '_{0}.jpg'.format(count)]))
            count = count + 1


    # 封装：从百度贴吧网页下载图片
    def download(self):
        html = self.getHtmlContent(self.url);
        jpgs = self.getJPGs(html);
        self.batchDownloadJPGs(jpgs,self.path)

    # 封装：从百度贴吧网页下载图片
    def downloadByBS(self):
        html = self.getHtmlContent(self.url);
        jpgs = self.getJPGsByBS(html);
        self.batchDownloadJPGs(jpgs, self.path)

    def setPath(self,path):
        self.path = path;

    def setUrl(self,url):
        self.url = url;

    def testMethod(self):
        print("aa");

    def jiandanDecode(m, r, d):
        # r = r ? r: "";
        # d = d ? d: 0;
        d = 0;
        q = 4;
        r = hashlib.md5(r);
        o = hashlib.md5(r.substr(0, 16));
        n = hashlib.md5(r.substr(16, 16));

        l = m.substr(0, q);
        c = o + hashlib.md5(o + l);

        m = m.substr(q);
        k = base64.b64decode(m);

        h = [];
        # for (g = 0; g < 256; g++) {
        for g in range(256):
            h[g] = g

        b = [];
        for g in range(256):
            b[g] = c.charCodeAt(g % c.length)


        for g in range(256):
            f = g;
            f = (f + h[g] + b[g]) % 256;
            tmp = h[g];
            h[g] = h[f];
            h[f] = tmp

        t = "";
        k = k.split("");
        for  g in range(k.length):
            p = f = g
            p = (p + 1) % 256;
            f = (f + h[p]) % 256;
            tmp = h[p];
            h[p] = h[f];
            h[f] = tmp;
            t += chr(ord(k[g]) ^ (h[(h[p] + h[f]) % 256]))

        t = t.substr(26)
        return t;


# dp = DownloadPagePic();
# dp.testMethod();
    # def main():
    #     url = 'http://tieba.baidu.com/p/2256306796'
    #     download(url)


if __name__ == '__main__':
    dp = JanDanCrawler();
    html = dp.getHtmlContent("https://jandan.net/ooxx");
    dp.getJPGsByBS(html);