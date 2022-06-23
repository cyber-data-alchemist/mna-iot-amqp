#!/usr/bin/env python
import pika, sys, os
from dotenv import load_dotenv
load_dotenv()

BROKER = os.getenv("BROKER")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

def main():
    credentials = pika.PlainCredentials(USER, PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = BROKER, credentials = credentials))
    channel = connection.channel()
    channel.queue_declare(queue = 'MNA-IOT')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue = 'MNA-IOT', on_message_callback = callback, auto_ack = True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted!')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)