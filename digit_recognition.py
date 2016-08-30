import webapp2
from google.appengine.api import images
from image_model import *
import handler as hd
from google.appengine.api import urlfetch
import json
import base64


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
        imgs = [(img.key.urlsafe(), img.label) for img in ret]
        nav = self.render_nav_str()
        self.render("digit_recognition.html",
                    imgs=imgs,
                    navigation=nav)

    def get_prediction(self, img):
        turi_key = "3b3e260a-69f8-406c-b4f3-65f29178d0ee"
        turi_key = base64.b64encode("admin_key:" + turi_key)
        turi_url = "http://my-ps-708303533.us-west-2.elb.amazonaws.com/query/predict_digit"
        headers = {"Authorization": "Basic %s" % turi_key}
        data = '{"data": {"img": %s}}' % json.dumps(img)
        result = urlfetch.fetch(url=turi_url,
                                payload=data,
                                method=urlfetch.POST,
                                headers=headers)
        result = json.loads(result.content)
        return result['response']

    def get(self):
        self.render_images()

    def post(self):
        file_upload = self.request.POST.get('attachment')
        blob = file_upload.file.read()
        blob = images.resize(blob, 480, 480)
        # todo: change img_str to the actual blob
        img_str = ["0"] * 64
        label = self.get_prediction(img_str)
        label = str(label)

        file_name = file_upload.filename
        img = ImageModel(id=file_name,
                         file_name=file_name,
                         blob=blob,
                         label=label)
        img.put()

        self.render_images()

app = webapp2.WSGIApplication([
    ('/digit_recognition', DigitRecognitionHandler),
    ('/img', ImageHandler)
], debug=True)
