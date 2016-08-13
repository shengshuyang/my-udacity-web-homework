import webapp2
import handler as hd
# import os
from validation_util import *
from blog_model import *


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


class BlogHandler(hd.Handler):

    def get(self):
        posts = db.GqlQuery(
            "select * from BlogPost order by created desc")
        self.render('blog.html', posts=posts)

    def post(self):
        self.redirect('/blog/new_post')

app = webapp2.WSGIApplication([
    ('/blog/?', BlogHandler),
    ('/blog/new_post', NewPostHandler),
    ('/blog/([0-9]+)', BlogPostHandler)
], debug=True)
