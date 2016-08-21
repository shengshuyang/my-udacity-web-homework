import webapp2
import handler as hd


class ThanksHandler(hd.Handler):
    def get(self):
        nav = self.render_nav_str()
        self.render('message.html', navigation=nav, message="Thank you!")

app = webapp2.WSGIApplication([
    ('/thanks', ThanksHandler)
], debug=True)
