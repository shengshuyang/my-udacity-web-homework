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
        items = self.request.get_all("item")
        user_input = self.request.get("user_input")
        content = get_html('/static/todo_list.html')
        items_html = ""
        for item in items:
            items_html += self.create_item(item)
        self.write_form(content%{"items":items_html, "user_input":user_input})

    def post(self):
        items = self.request.get_all("item")
        new_item = self.request.get("user_input")
        items.append(new_item)
        items_html = ""
        for item in items:
            items_html += self.create_item(item)

        args = "item="+new_item
        url = self.request.url
        if "?" not in url:
            url += "?"+args
        else:
            url += "&"+args

        self.redirect(url.encode('ascii','ignore'))
        #self.redirect("welcome?username="+i_name)

app = webapp2.WSGIApplication([
    ('/todo_list', ToDoHandler)
], debug=True)