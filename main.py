#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import cgi

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    if month.title() in months:
        return month.title()
    return None

def valid_day(day):
    if not day.isdigit():
        return None
    day = int(day)
    if day > 0 and day <= 31:
        return day
    return None

def valid_year(year):
    if not year.isdigit():
        return None
    year = int(year)
    if year <= 2020 and year >= 1900:
        return year
    return None

def get_html(path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    index_path =  dir_path+path
    return open(index_path).read()

# def escape_html(s):
#     if type(s) is not str:
#         s = str(s)
#     return s.replace('&','&amp;').\
#         replace('>', '&gt;').\
#         replace('<','&lt;').\
#         replace('"','&quot;')

def escape_html(s):
    if type(s) is not str:
        s = str(s)
    return cgi.escape(s, quote = True).encode('ascii','ignore')


###################################
class MainHandler(webapp2.RequestHandler):
    def write_form(self, form, error="", month="", day="", year=""):
        self.response.out.write(form % {
          "error" : error,
          "month" : month,
          "day" : day,
          "year" : year})

    def get(self):
        content = get_html('/static/index.html')
        self.write_form(content)

    def post(self):
        i_m = self.request.get("month")
        i_d = self.request.get("day")
        i_y = self.request.get("year")
        m = valid_month(i_m)
        d = valid_day(i_d)
        y = valid_year(i_y)
        if not (m and d and y):
            content = get_html('/static/index.html')
            self.write_form(content,
              error="Something Wrong",
              month=escape_html(i_m),
              day=escape_html(i_d),
              year=escape_html(i_y))
        else:
            self.redirect("/thanks")

###################################
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thank you!")

###################################
class SignupHandler(webapp2.RequestHandler):
    def write_form(self, form, error="", username="", \
                    pswd="", pswd2="", email=""):
        self.response.out.write(form % {
          "error" : error,
          "username" : username,
          "pswd" : pswd,
          "pswd2" : pswd2,
          "email" : email})

    def get(self):
        content = get_html('/static/signup.html')
        self.write_form(content)

    def post(self):
        i_name = self.request.get("username").encode('ascii','ignore')
        self.redirect("welcome?username="+i_name)


###################################
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        msg = "Thank you, "+username+" !"
        content = get_html('/static/message.html')
        self.response.out.write(content%{"message":msg})

###################################
# class TestHandler(webapp2.RequestHandler):
#     def write_form(self, form, error=""):
#         self.response.out.write(form % {"error" : error})

#     def get(self):
#         q = self.request.get("q")
#         self.response.out.write(q)

#     def post(self):
#         m = valid_month(self.request.get("month"))
#         d = valid_day(self.request.get("day"))
#         y = valid_year(self.request.get("year"))
#         if not (m and d and y):
#             content = get_index()
#             self.write_form(content, "Something Wrong")
#         else:
#             self.response.out.write("Thank you!")

        # self.response.headers['content-type'] = "text/plain"
        # self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomeHandler)
    #('/testform', TestHandler)
], debug=True)
