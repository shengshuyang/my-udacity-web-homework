import webapp2
import handler as hd


class WelcomeHandler(hd.Handler):
    def get(self):
        nav = self.render_nav_str()
        cookie = self.request.cookies.get('user')
        username = cookie.split("|")[0]
        msg = "Welcome, %s !" % username
        self.render('message.html', navigation=nav, message=msg)

app = webapp2.WSGIApplication([
    ('/welcome', WelcomeHandler)
], debug=True)
