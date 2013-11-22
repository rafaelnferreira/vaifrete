import datetime
import time
import logging
from protorpc import remote
from protorpc import messages
from models import *

class Delivery(messages.Message):
    destination_address = messages.StringField(1, required=True)
    dest_lat = messages.StringField(2)
    dest_lng = messages.StringField(3)
    source_address = messages.StringField(4)
    source_lat = messages.StringField(5)
    source_lng =messages.StringField(6)
    request_user = messages.StringField(7)

class Deliveries(messages.Message):
    deliveries = messages.MessageField(Delivery, 1, repeated=True)

class GetDeliveriesRequest(messages.Message):
    limit = messages.IntegerField(1, default=10)
    user = messages.StringField(2)
  
class DeliveryService(remote.Service):
    @remote.method(GetDeliveriesRequest, Deliveries)
    def get_deliveries(self, request):
        logging.debug('Received request ' + str(request))

        query = DeliverFee.all().order('-request_date_time')
  
        #if request.user:
            #query.filter('date <=', when)
  
        deliveries = []
        for delivery_model in query.fetch(request.limit):
            delivery = Delivery(destination_address=delivery_model.destination_address, dest_lat=delivery_model.dest_lat, dest_lng=delivery_model.dest_lng, source_address=delivery_model.source_address, source_lat=delivery_model.source_lat, source_lng=delivery_model.source_lng, request_user=delivery_model.request_user.email())
            deliveries.append(delivery)
        
        return Deliveries(deliveries=deliveries)