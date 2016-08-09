import webapp2
import os
import re
from validation_util import *

patterns = {'username' : r"^[a-zA-Z0-9_-]{3,20}$",
            "password" : r"^.{3,20}$",
            "email" : r"^[\S]+@[\S]+.[\S]+$"}

def match_regex(pattern, input):
    facto = re.compile(pattern)
    return facto.match(input)

class SignupHandler(webapp2.RequestHandler):
    def write_form(self, form, username="", \
                    pswd="", pswd2="", email="", \
                    err1="",err2="",err3="",err4=""):
        self.response.out.write(form % {
          "username" : username,
          "pswd" : pswd,
          "pswd2" : pswd2,
          "email" : email,
          "err1" : err1,
          "err2" : err2,
          "err3" : err3,
          "err4" : err4})

    def get(self):
        content = get_html('/templates/signup.html')
        self.write_form(content)

    def post(self):
        i_name = self.request.get("username").encode('ascii','ignore')
        i_pswd = self.request.get("pswd").encode('ascii','ignore')
        i_pswd2 = self.request.get("pswd2").encode('ascii','ignore')
        i_email = self.request.get("email").encode('ascii','ignore')
        errs = ["" for i in range(4)]
        if match_regex(patterns["username"],i_name) is None:
            errs[0] = "That's not a valid username."
        if match_regex(patterns["password"],i_pswd) is None:
            errs[1] = "That's not a valid password."
        if i_pswd != i_pswd2:
            errs[2] = "Your passwords didn't match."
        if match_regex(patterns["email"],i_email) is None:
            errs[3] = "That's not a valid email address."
        for err in errs:
            if err != "":
                content = get_html('/templates/signup.html')
                self.write_form(content, i_name, i_pswd, i_pswd2,
                    i_email, errs[0],errs[1],errs[2],errs[3])
                return
        self.redirect("welcome?username="+i_name)

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler)
], debug=True)
