#!/usr/bin/env python
import time
import pika
import zlib

# start a connection with localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

#img reading
IMGPATH = './sample_img.jpg'
image = None

with open(IMGPATH, 'rb') as img:
	image = img.read()
	
#compress image
print('original size: '+str(len(image)))
image = zlib.compress(image)
print('compressed size: '+str(len(image)))

#loop to send image
while(True):
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=image)
	print('image size sent = ' + str(len(image)))
	time.sleep(0.04)


# close connection
connection.close()