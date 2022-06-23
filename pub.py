#!/usr/bin/env python
import pika, sys, os
from dotenv import load_dotenv
load_dotenv()

BROKER = os.getenv("BROKER")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

credentials = pika.PlainCredentials(USER, PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(host = BROKER, credentials = credentials))
channel = connection.channel()
channel.queue_declare(queue = 'MNA-IOT')

try:
    while True:
        msg = input("Type your message: ")
        channel.basic_publish(exchange = '', routing_key = 'MNA-IOT', body = msg)
except KeyboardInterrupt:
    connection.close()
    print('interrupted!')


