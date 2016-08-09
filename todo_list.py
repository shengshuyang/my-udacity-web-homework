import webapp2
import jinja2
import handler as hd
import os

class ToDoHandler(hd.Handler):

    def get(self):
        self.render("todo_list.html",
            items=self.request.get_all("food"))

app = webapp2.WSGIApplication([
    ('/todo_list', ToDoHandler)
], debug=True)