import webapp2
import os
import re
import handler as hd
from validation_util import *

patterns = {'username' : r"^[a-zA-Z0-9_-]{3,20}$",
            "password" : r"^.{3,20}$",
            "email" : r"^[\S]+@[\S]+.[\S]+$"}

def match_regex(pattern, input):
    facto = re.compile(pattern)
    return facto.match(input)

class SignupHandler(hd.Handler):

    def get(self):
        self.render("signup.html",
            items=self.request.get("food"))

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
        if i_email and match_regex(patterns["email"],i_email) is None:
            errs[3] = "That's not a valid email address."
        for err in errs:
            if err != "":
                self.render("signup.html",
                    username=i_name,
                    pswd=i_pswd,
                    pswd2=i_pswd2,
                    email=i_email,
                    err1=errs[0],
                    err2=errs[1],
                    err3=errs[2],
                    err4=errs[3])
                return
        self.redirect("welcome?username="+i_name)

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler)
], debug=True)
