import webapp2
import handler as hd


class WelcomeHandler(hd.Handler):
    def get(self):
        input_name = self.request.get("username")
        cookie = self.request.cookies.get('user')
        if input_name:
            msg = "Welcome, %s !" % input_name
        elif cookie:
            username = cookie.split("|")[0]
            msg = "Welcome, %s !" % username
        else:
            msg = ""
        self.render('message.html', message=msg)

app = webapp2.WSGIApplication([
    ('/welcome', WelcomeHandler)
], debug=True)
