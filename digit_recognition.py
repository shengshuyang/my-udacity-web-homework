import webapp2
from google.appengine.api import images
from image_model import *
import handler as hd
from google.appengine.api import files, images


class ImageHandler(hd.Handler):
    def get(self):
        image_key = ndb.Key(urlsafe=self.request.get('img_id'))
        img = image_key.get()
        if img.blob:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(img.blob)
        else:
            self.response.out.write('No image')


class DigitRecognitionHandler(hd.Handler):

    def render_images(self):
        nav = self.render_nav_str()
        ret = ImageModel.query().order(-ImageModel.date).fetch(8)
        imgs = [img.key.urlsafe() for img in ret]
        nav = self.render_nav_str()
        self.render("digit_recognition.html",
                    imgs=imgs,
                    navigation=nav)

    def get(self):
        self.render_images()

    def post(self):
        file_upload = self.request.POST.get('attachment')
        blob = file_upload.file.read()
        file_name = file_upload.filename
        img = ImageModel(id=file_name,
                           file_name=file_name,
                           blob=blob)
        img.put()
        self.render_images()

app = webapp2.WSGIApplication([
    ('/digit_recognition', DigitRecognitionHandler),
    ('/img', ImageHandler)
], debug=True)
