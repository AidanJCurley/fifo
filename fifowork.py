import os


def send_write():
    send = open('temp', 'w')
    while True:
        usrin = input('input text to send to fifo: ')
        send.write(usrin)
        send.flush()


def read():
    os.system('cat temp')