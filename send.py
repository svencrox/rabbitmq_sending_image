#!/usr/bin/env python
import pika

# start a connection with localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

#sending hello world with routing key which refers to queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# close connection
connection.close()