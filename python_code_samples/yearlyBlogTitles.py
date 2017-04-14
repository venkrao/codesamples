#!/usr/bin/env python

"""
Write a cli application in python that takes one argument(year, default: current year) 
and prints out the all blog titles from our blog for that given year.

https://www.paessler.com/blog

"""
import sys
import datetime
import requests
import re


class BlogCrawler:
   def __init__(self, url):
      self.url = url
      self.response = requests.get(url)

   def get_response_object(self, url):
      return requests.get(url)

   def get_response_text(self):
      return self.response.text

   def get_status_code(self):
      return self.response.status_code

   def is404(self):
      return (404 == self.response.status_code)

   def get_titles(self, text):
       # Well, jump right to it.
       overview_blog = '\<div class=\"overview-blog\"\>'
       meta = '\<div class=\"meta\"\>'
       h3 = '\<h3\>'
       anchor_start = '\<a'
       angle_right = '\>'
       anchor_end = '\</a\>'

       # Working: \<div class=\"overview-blog\"\>\n<div class=\"meta\">.*\n.*\n.*\n.*\n.+?>(\w.*)</a>
       # Refined: \<div class=\"overview-blog\"\>\n<div class=\"meta\">\n.+?\n.+?\n.+?\n.+?>(\w.*)</a>

       # regex = re.compile('\<div class=\"overview-blog\"\>\n<div class=\"meta\">\n.+?\n.+?\n.+?\n.+?>(\w.*)</a>')
       regex = re.compile('<div class=\"overview-blog\">\n?<div class=\"meta\">\n?<img.+?>\n<p>\n.+?\n<a.+?\n.*\n.+?\n.*\n.+?\n.+?\n<h3><a.+?>(.+?)</a></h3>')

       titles = regex.findall(text)
       return titles

   @classmethod 
   def get_page_url(self, baseurl, year, page):
       return baseurl + year + "/page/%s/" %(page) 


if __name__ == "__main__":
   if len(sys.argv) == 1:
      print "No argument 1. Assuming current year as desired year."
      year = datetime.datetime.now().strftime("%Y")
   else:
      year = sys.argv[1]
      
   baseurl = "https://www.paessler.com/blog/"
   page = 1
   endofposts = False
   print "post titles from %s\n-------" %(year)
   while not endofposts:
      year_crawler = BlogCrawler(BlogCrawler.get_page_url(baseurl, year, page))
      if year_crawler.is404():
         endofposts = True
      else:
          titles = year_crawler.get_titles(year_crawler.get_response_text())
          if titles:
             for t in titles:
               print t
          page += 1
