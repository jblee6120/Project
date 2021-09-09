import json
from random import randint
from channels.generic.websocket import WebsocketConsumer
from time import sleep
import serial
from .models import *
class WSconsumer(WebsocketConsumer):
    def connect(self):

        self.accept()

        ser = serial.Serial('COM3', '9600')

        for i in range(10):
            if ser.readable():
                coor = ser.readline()
                coordinate = int(coor.decode())
                self.send(json.dumps({'message': coordinate}))

    def disconnect(self, close_code):
        self.close(self)

"""
class LoadBooks(WebsocketConsumer):
    def connect(self):
        self.accept()

        booklist = [None]*5

        for i in len(booklist):
            barcode = request.GET.get('barcode')
            if barcode:
                booklist[i] = BookList.objects.filter(barcode__icontains = barcode)
                self.send(json.dumps(booklist[i]))
"""