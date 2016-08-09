import webapp2
import os
import re
from validation_util import *

class ToDoHandler(webapp2.RequestHandler):
    def write_form(self, form, item=""):
        self.response.out.write(form % {
          "item" : item})

    def get(self):
        content = get_html('/static/todo_list.html')
        self.write_form(content)

    def post(self):
        self.redirect("welcome?username="+i_name)

app = webapp2.WSGIApplication([
    ('/todo_list', ToDoHandler)
], debug=True)