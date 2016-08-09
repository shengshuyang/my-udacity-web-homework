import webapp2
import os
from validation_util import *

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        content = get_html('/static/message.html')
        self.response.out.write(content%{"message":"Thank you!"})

app = webapp2.WSGIApplication([
    ('/thanks', ThanksHandler)
    #('/testform', TestHandler)
], debug=True)
