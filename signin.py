import webapp2
import handler as hd
from user_model import *
from validation_util import *


class SigninHandler(hd.Handler):

    def get_form_input(self, s):
            return self.request.get(s).encode('ascii', 'ignore')

    def get(self):
        nav = self.render_str("nav_off.html")
        self.render("signin.html", navigation=nav)

    def post(self):
        i_name = self.get_form_input("username")
        i_pswd = self.get_form_input("pswd")
        err1, err2 = "", ""
        if not i_name:
            err1 = "please input your username"
        if not i_pswd:
            err2 = "password cannot be empty"
        if err1 or err2:
            self.render("signin.html",
                        username=i_name,
                        password=i_pswd,
                        err1=err1, err2=err2)
            return
        user = db.GqlQuery("select * from User where username = :1", i_name)
        user = user[0]
        if valid_pw(i_name, i_pswd, user.password):
            user_hash = "%s|%s" % (i_name, user.password)
            self.response.headers.add_header(
                    'Set-Cookie', 'user=%s' % user_hash.encode('ascii', 'ignore'))
            self.redirect("welcome")
        else:
            nav = self.render_str("nav_off.html")
            self.render("signin.html",
                        navigation=nav,
                        username=i_name,
                        password=i_pswd,
                        err2="incorrect password")

app = webapp2.WSGIApplication([
    ('/signin', SigninHandler)
], debug=True)
