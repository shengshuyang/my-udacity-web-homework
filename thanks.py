import webapp2
import os
import handler as hd
from validation_util import *

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.render('message.html', message = "Thank you")

app = webapp2.WSGIApplication([
    ('/thanks', ThanksHandler)
], debug=True)
