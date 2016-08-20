import webapp2
import re
import handler as hd
from user_model import *
from validation_util import *

patterns = {'username': r"^[a-zA-Z0-9_-]{3,20}$",
            "password": r"^.{3,20}$",
            "email": r"^[\S]+@[\S]+.[\S]+$"}


def match_regex(pattern, input):
    facto = re.compile(pattern)
    return facto.match(input)


class SignupHandler(hd.Handler):

    def get_form_input(self, s):
            return self.request.get(s).encode('ascii', 'ignore')

    def validate_form(self, cache):
        print cache
        errs = ["" for i in range(4)]
        if match_regex(patterns["username"], cache["username"]) is None:
            errs[0] = "That's not a valid username."
        if match_regex(patterns["password"], cache["password"]) is None:
            errs[1] = "That's not a valid password."
        if cache["password"] != cache["password2"]:
            errs[2] = "Your passwords didn't match."
        if cache["email"] and match_regex(patterns["email"], cache["email"]) is None:
            errs[3] = "That's not a valid email address."
        return errs

    def get(self):
        self.render("signup.html")

    def post(self):
        user_input = {}
        user_input["username"] = self.get_form_input("username")
        user_input["password"] = self.get_form_input("pswd")
        user_input["password2"] = self.get_form_input("pswd2")
        user_input["email"] = self.get_form_input("email")
        print user_input
        errs = self.validate_form(user_input)
        user = db.GqlQuery("select * from User where username = :1", user_input["username"] )
        if user.count() > 0:
            errs[0] = "user already exists"
        for err in errs:
            if err != "":
                self.render("signup.html",
                            username=user_input["username"],
                            pswd=user_input["password"],
                            pswd2=user_input["password2"],
                            email=user_input["email"],
                            err1=errs[0],
                            err2=errs[1],
                            err3=errs[2],
                            err4=errs[3])
                return
        pw_hash = make_pw_hash(user_input["username"], user_input["password"])
        user_hash = "%s|%s" % (user_input["username"], pw_hash)
        self.response.headers.add_header(
                'Set-Cookie', 'user=%s' % user_hash.encode('ascii', 'ignore'))
        user = User(username=user_input["username"],
                    password=pw_hash,
                    email=user_input["email"])
        user.put()
        self.redirect("welcome")

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler)
], debug=True)
