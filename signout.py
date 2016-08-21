import webapp2
import handler as hd
from validation_util import *


class SignOutHandler(hd.Handler):

    def get(self):
        self.response.set_cookie(key='user', value=None)
        self.redirect("/")


app = webapp2.WSGIApplication([
    ('/signout', SignOutHandler)
    ], debug=True)