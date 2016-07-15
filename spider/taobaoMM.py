#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zh_octopus
# @Date:   2016-07-15 12:54:07
# @Last Modified by:   zh_octopus
# @Last Modified time: 2016-07-15 13:03:34

import urllib2
import re

class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
 
    def getPage(self,pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        #print page
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2],item[3],item[4]
 
spider = Spider()
spider.getContents(1)