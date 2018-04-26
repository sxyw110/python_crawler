#!/usr/bin/python
# coding:utf-8
# 实现一个简单的爬虫，爬取百度贴吧图片
import urllib.request
import re

import DownloadPagePic

def getUrlList(url):
    dp = DownloadPagePic("12","34");
    html = dp.getHtmlContent(url);
    # html = html.decode


def getUrls(html):

    urlReg = re.compile('href="(.*?)"');

    # html = html.decode("utf-8");
    urls = re.findall(urlReg, html);
    print(urls);

if __name__ == '__main__':
    getUrls("<a rel=\"noreferrer\" href=\"/p/5666211348\" title=\"记录一下\" target=\"_blank\" class=\"j_th_tit\"  href=\"/p/5666211349\" clicked=\"true\">记录一下</a>");