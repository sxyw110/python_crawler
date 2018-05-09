#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取图片
import urllib.request
import re
import os, sys
from bs4 import BeautifulSoup
import hashlib
import base64
import time

class JanDanCrawler:
    path = '';
    url = "";

    def getHtmlContent(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        page = urllib.request.urlopen(req);
        return page.read()



    def getJPGCodesByBS(self, html):
        soup = BeautifulSoup(html, "html.parser");
        print(soup);
        spans = soup.find_all('span',class_="img-hash");
        
        jpgCodes =[];
        for span in spans:
            jpgCodes.append(span.string);
        print(jpgCodes);
        print( len(jpgCodes));
        return jpgCodes;

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


    def batchDownloadJPGs(self,imgUrls,pageNO, path='D://crawler//'):
        # 用于给图片命名
        count = 1
        self.mkdirs(path);
        for url in imgUrls:
            self.downloadJPG(url, ''.join([path, '{1}_{0}.jpg'.format(count,base64.b64encode(url.encode("utf-8")))]))
            count = count + 1
            time.sleep(0.1);


    def download(self):
        html = self.getHtmlContent(self.url);
        jpgs = self.getJPGs(html);
        self.batchDownloadJPGs(jpgs,self.path)

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

    def parse(self,imgHash, constant):
        q = 4
        hashlib.md5()
        constant = self.md5(constant)
        o = self.md5(constant[0:16])
        n = self.md5(constant[16:32])
        l = imgHash[0:q]
        c = o + self.md5(o + l)
        imgHash = imgHash[q:]
        k = self.decode_base64(imgHash)
        h = list(range(256))

        b = list(range(256))

        for g in range(0, 256):
            b[g] = ord(c[g % len(c)])

        f = 0
        for g in range(0, 256):
            f = (f + h[g] + b[g]) % 256
            tmp = h[g]
            h[g] = h[f]
            h[f] = tmp

        print(k);
        print(g);
        result = ""
        p = 0
        f = 0
        for g in range(0, len(k)):
            p = (p + 1) % 256;
            f = (f + h[p]) % 256
            tmp = h[p]
            h[p] = h[f]
            h[f] = tmp
            result += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
        result = result[26:]
        return result

    def md5(self,value):
        m2 = hashlib.md5()
        m2.update(value.encode("utf-8"));
        return m2.hexdigest();

    def decode_base64(self,data):
        missing_padding = 4 - len(data) % 4
        if missing_padding:
            data += '=' * missing_padding
        return base64.b64decode(data)

# dp = DownloadPagePic();
# dp.testMethod();
    # def main():
    #     url = 'http://tieba.baidu.com/p/2256306796'
    #     download(url)


    def downloadPic(self,pageNO):
        url = "https://jandan.net/ooxx/page-"+str(pageNO)+"#comments";

        html = dp.getHtmlContent(url);
        imgCode = dp.getJPGCodesByBS(html);

        imgUrls = [];
        for code in imgCode:
            url = dp.parse(code, "H5C7UxNkap5ZxckFrL8PSljODZxgpH37");
            imgUrls.append("http:" + url.replace("mw600", "large"));
        print(imgUrls);
        dp.batchDownloadJPGs(imgUrls,pageNO);

if __name__ == '__main__':
    dp = JanDanCrawler();

    page = 65;
    size = 10;

    for current in range((page -size),page):
        dp.downloadPic(current);
        time.sleep(3);


