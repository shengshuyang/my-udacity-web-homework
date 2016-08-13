import webapp2
import handler as hd
# import os
from validation_util import *
from blog_model import *
import hashlib

class BlogPostHandler(hd.Handler):

    def get(self, post_id):
        key = db.Key.from_path('BlogPost', int(post_id))
        post = db.get(key)
        if not post:
            self.render('message.html', message="Post doesn't exist.")
        else:
            self.render('blog_post.html', title=post.title, content=post.content)


class NewPostHandler(hd.Handler):

    def get(self):
        self.render('new_post.html')

    def post(self):
        title = self.request.get("title")
        content = self.request.get("content")
        if title and content:
            a = BlogPost(title=title, content=content)
            a.put()
            post_id = a.key().id()
            self.redirect('/blog/%s' % str(post_id))
        else:
            self.render("new_blog.html",
                        error="Something wrong.",
                        title=title,
                        content=content)

def hash_str(s):
    return hashlib.md5(s).hexdigest()

def make_secure_val(s):
    return "%s|%s" %(s, hash_str(s)) 

def check_secure_val(h):
    val = h.split("|")[0]
    if make_secure_val(val) == h:
        return val

class BlogHandler(hd.Handler):

    def get(self):
        posts = db.GqlQuery(
            "select * from BlogPost order by created desc")
        cookie_str = self.request.cookies.get('visits')
        visits = 0
        if cookie_str:
            cookie_val = check_secure_val(cookie_str)
            if cookie_val:
                visits = int(cookie_val)
            else:
                self.render("message.html", message=cookie_str)
                return
        visits += 1
        self.response.headers.add_header('Set-Cookie', 'visits=%s' % make_secure_val(str(visits)))
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.render('blog.html', posts=posts, visits=self.response.headers)
        self.render('blog.html', posts=posts, visits= "Visit Count: %s" % visits)

    def post(self):
        self.redirect('/blog/new_post')

app = webapp2.WSGIApplication([
    ('/blog/?', BlogHandler),
    ('/blog/new_post', NewPostHandler),
    ('/blog/([0-9]+)', BlogPostHandler)
], debug=True)
