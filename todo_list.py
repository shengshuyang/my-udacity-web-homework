import webapp2
import os
import re
from validation_util import *

class ToDoHandler(webapp2.RequestHandler):

    def create_item(self, item):
         return "<tr><th>%(item)s</th></tr>"%{"item":item}

    def write_form(self, form, items="", user_input=""):
        self.response.out.write(form % {
          "items" : items,
          "user_input" : user_input})

    def get(self):
        content = get_html('/static/todo_list.html')
        self.write_form(content)

    def post(self):
        item = self.request.get("user_input")
        item = self.create_item(item)
        content = get_html('/static/todo_list.html')
        self.write_form(content, items = item)
        #self.redirect("welcome?username="+i_name)

app = webapp2.WSGIApplication([
    ('/todo_list', ToDoHandler)
], debug=True)