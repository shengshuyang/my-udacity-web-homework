import webapp2
import os
import handler as hd
from validation_util import *

class WelcomeHandler(hd.Handler):
    def get(self):
        username = self.request.get("username")
        msg = "Welcome, "+username+" !"
        self.render('message.html', message = msg)

app = webapp2.WSGIApplication([
    ('/welcome', WelcomeHandler)
], debug=True)
