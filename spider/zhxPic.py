#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zh_octopus
# @Date:   2016-07-15 12:54:07
# @Last Modified by:   zh_octopus
# @Last Modified time: 2016-07-15 13:03:59

import urllib2
import urllib
import re
import cookielib
import time


class DownFromSour:
    def __init__(self):
        self.siteURL = 'http://www.kuailehu.cn'
        self.SourceFile = 'zhxPictureSource.txt'

    def GetSource(self):
        f = open(self.SourceFile, 'r')
        try:
            return f.read()
        finally:
            f.close()

    def DownFile(self, imageURL, fileName):

        # 构造Header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.1.1000 Chrome/39.0.2146.0 Safari/537.36',
            'Referer': 'http://www.kuailehu.cn/index.do'}

        request = urllib2.Request(imageURL, None, headers)

        u = urllib2.urlopen(request, timeout=15)
        #u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u"正在保存图片为", fileName
        f.close()

    #获取所有照片
    def DownAllImg(self, fromIdx):
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        page = self.GetSource()
        items = re.findall(patternImg, page)
        print u"总共有%d张图片" %(len(items))
        index = 0
        for item in items:
            if index < fromIdx:
                index += 1
                continue
            imgUrl = self.siteURL + '/' + item
            fileName = 'zhxPic/' + str(index) + '.jpg'
            self.DownFile(imgUrl, fileName)
            index += 1


DownImp = DownFromSour()
DownImp.DownAllImg(104)

