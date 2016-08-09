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
from validation_util import *

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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
