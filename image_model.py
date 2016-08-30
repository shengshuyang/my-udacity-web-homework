from google.appengine.ext import ndb


class ImageModel(ndb.Model):
    blob = ndb.BlobProperty()
    file_name = ndb.StringProperty()
    label = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
