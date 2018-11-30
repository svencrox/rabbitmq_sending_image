#!/usr/bin/env python
import pika

# start a connection with localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

#img reading
IMGPATH = './sample_img.jpg'

with open(IMGPATH, 'rb') as img:
	image = img.read()
	#sending hello world with routing key which refers to queue
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=image)
	print('image size = ' + str(len(image)))

# close connection
connection.close()