import webapp2
import handler as hd
# import os
from validation_util import *
from blog_model import *


class NewBlogHandler(hd.Handler):

    def get(self):
        self.render('new_blog.html')

    def post(self):
        title = self.request.get("title")
        content = self.request.get("content")
        if title and content:
            a = BlogPost(title=title, content=content)
            a.put()
            self.redirect('/blog')
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
        self.redirect('/new_blog')

app = webapp2.WSGIApplication([
    ('/blog', BlogHandler),
    ('/new_blog', NewBlogHandler)
], debug=True)
