#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 常用内建模块->HTMLParser
# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。

from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint

def fetch_data(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        return f.read().decode('utf-8')

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.flag = None
        self.event_info = {}
        self.event_list = []

    def handle_starttag(self, tag, attrs):
        # print('starttag: %s, attrs: %s' % (tag, str(attrs)))
        if ('class', 'event-title') in attrs:
            self.flag = 'title'
        if 'time' == tag:
            self.flag = 'time'
        if ('class', 'event-location') in attrs:
            self.flag = 'location'

    def handle_endtag(self, tag):
        # print('</%s>' % tag)
        # pass
        self.flag = ''

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        pass

    def handle_data(self, data):
        # print(data)
        if self.flag in ('title', 'time', 'location'):
            self.event_info[self.flag] = data

        if len(self.event_info) == 3:
            self.event_list.append(self.event_info)
            self.event_info = {}

        # if self.flag == 'title':
        #     self.event_info['title'] = data
        #     self.flag = 0
        #
        # if self.flag == 'time':
        #     self.event_info['time'] = data
        #     self.flag = 0
        #
        # if self.flag == 'location':
        #     self.event_info['location'] = data
        #     self.flag = 0
        #     self.event_list.append(self.event_info)
        #     self.event_info = {}

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass

    def print_info(self):
        for n in self.event_list:
            print('title: %s' % n['title'])
            print('time: %s' % n['time'])
            print('location: %s' % n['location'])
            print('-----------------------------------------------------')

# 测试:
URL = 'https://www.python.org/events/python-events/'
data = fetch_data(URL)
# print(data)
parser = MyHTMLParser()
parser.feed(data)
parser.print_info()