import webapp2
import jinja2
import os
from user_model import *


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True)

jinja_env.filters["datetimeformat"] = datetimeformat


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **params):
        self.write(self.render_str(template, **params))

    def is_signed_in(self):
        cookie = self.request.cookies.get("user")
        print "local:", cookie
        if not cookie:
            return False
        local_name, local_pswd = cookie.split("|")
        user = db.GqlQuery("select * from User where username = :1", local_name)
        if user.count() != 1:
            return False
        user = user[0]
        print "%s|%s", (user.username, user.password)
        if local_pswd == user.password.encode('ascii', 'ignore'):
            return True
        return False

    def render_nav_str(self):
        if self.is_signed_in():
            return self.render_str("nav_on.html")
        else:
            return self.render_str("nav_off.html")