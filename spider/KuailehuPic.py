#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zh_octopus
# @Date:   2016-07-15 12:54:07
# @Last Modified by:   zh_octopus
# @Last Modified time: 2016-07-15 13:03:36

import urllib2
import urllib
import re
import cookielib
import time


class Spider:
    def __init__(self):
        self.siteURL = 'http://www.kuailehu.cn'

    def login(self):
        hosturl = self.siteURL
        loginurl = self.siteURL + '/login.do'
        print loginurl
        #设置cookie处理器
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

        #打开登录页面
        h = urllib2.urlopen(hosturl)

        #构造Header
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.1.1000 Chrome/39.0.2146.0 Safari/537.36',
                   'Referer' : 'http://www.kuailehu.cn/index.do'}

        #构造post数据
        postData = {'account' : '13527211121','pass' : '12345678', time.time() : 'date'}
        postData = urllib.urlencode(postData)

        request = urllib2.Request(loginurl, postData, headers)
        #print request
        response = urllib2.urlopen(request)
        text = response.read()
        print text

        '''Listurl = self.siteURL + "/picType/myList.do"
        print Listurl
        request = urllib2.Request(Listurl)
        response = urllib2.urlopen(request)
        text = response.read()
        print text'''


    def getMyAlbum(self):
        url = self.siteURL + "/picType/myList.do"
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def getContents(self):
        page = self.getMyAlbum()
        print page
        '''pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item[0], item[1], item[2], item[3], item[4]'''


spider = Spider()
spider.login()