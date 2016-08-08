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

def get_index():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    index_path =  dir_path+'/static/index.html'
    return open(index_path).read()

###################################
class MainHandler(webapp2.RequestHandler):
    def write_form(self, form, error=""):
        self.response.out.write(form % {"error" : error})

    def get(self):
        content = get_index()
        self.write_form(content)

###################################
class TestHandler(webapp2.RequestHandler):
    def write_form(self, form, error=""):
        self.response.out.write(form % {"error" : error})

    def get(self):
        q = self.request.get("q")
        self.response.out.write(q)

    def post(self):
        m = valid_month(self.request.get("month"))
        d = valid_day(self.request.get("day"))
        y = valid_year(self.request.get("year"))
        if not (m and d and y):
            content = get_index()
            self.write_form(content, "Something Wrong")
        else:
            self.response.out.write("Thank you!")

        # self.response.headers['content-type'] = "text/plain"
        # self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)
