import webapp2
import os
from validation_util import *

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        msg = "Thank you, "+username+" !"
        content = get_html('/static/message.html')
        self.response.out.write(content%{"message":msg})

app = webapp2.WSGIApplication([
    ('/welcome', WelcomeHandler)
], debug=True)
