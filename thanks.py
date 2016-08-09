import webapp2
import handler as hd

class ThanksHandler(hd.Handler):
    def get(self):
        self.render('message.html', message = "Thank you!")

app = webapp2.WSGIApplication([
    ('/thanks', ThanksHandler)
], debug=True)
