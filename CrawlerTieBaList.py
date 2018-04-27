#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取百度贴吧图片
import urllib.request
import re

from DownloadPagePic import *

def getUrlList(url):
    dp = DownloadPagePic();
    html = dp.getHtmlContent(url);
    # print(html);
    urls = getUrls(html);


    print(urls);

    urlPre = "http://tieba.baidu.com";
    pathPre = "D://crawler";

    for url in urls:
        dp.setPath(pathPre + url);
        dp.setUrl(urlPre + url);
        dp.download();


    # html = html.decode


def getUrls(html):


    html = html.decode("utf-8");
    # print(html);

    htmlContentReg = re.compile('<ul id="thread_list" class="threadlist_bright j_threadlist_bright">(.*)<div class="thread_list_bottom clearfix">',re.S);
    htmlContent = re.findall(htmlContentReg, html);
    print(htmlContent);

    urlReg = re.compile('<a rel=\"noreferrer\"  href="([^:]*?)" title=');
    urls = re.findall(urlReg, htmlContent[0]);
    return urls;

if __name__ == '__main__':
    getUrlList("http://tieba.baidu.com/f?kw=%E6%91%84%E5%BD%B1");