import webapp2
import handler as hd
# import os
from validation_util import *
from art_model import *


class AsciiChanHandler(hd.Handler):
    def render_page(self, error="", title="", art=""):
        arts = db.GqlQuery(
            "select * from Art order by created desc")

        self.render("ascii_chan.html",
                    error=error,
                    title=title,
                    art=art,
                    arts=arts)

    def get(self):
        self.render('ascii_chan.html')

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if title and art:
            a = Art(title=title, art=art)
            a.put()
            self.render_page(error="", title=title, art=art)
        else:
            self.render_page(error="Something wrong.",
                             title=title,
                             art=art)

app = webapp2.WSGIApplication([
    ('/ascii_chan', AsciiChanHandler)
], debug=True)
