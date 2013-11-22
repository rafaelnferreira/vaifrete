
from google.appengine.ext import db

class AppUser(db.Model):
  real_user = db.UserProperty()
  vehicle = db.StringProperty()
  user_type = db.StringProperty()
  last_status = db.StringProperty()
  last_position = db.StringProperty()

class DeliverFee(db.Model):
	source_address = db.StringProperty()
	destination_address = db.StringProperty()
	request_user = db.UserProperty()
	item = db.StringProperty()
	request_date_time = db.DateTimeProperty()
	closed = db.BooleanProperty()
	source_lat = db.StringProperty()
	source_lng = db.StringProperty()
	dest_lat = db.StringProperty()
	dest_lng = db.StringProperty()