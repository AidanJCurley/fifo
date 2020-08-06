
def read():
    FIFO_PATH = input('input the path of your fifo')
    fifo = open(FIFO_PATH, 'r')
    while True:
        print(fifo.readline())


def send_write():
    FIFO_PATH2 = input('input the path of your fifo')
    send = open(FIFO_PATH2, 'w+')
    while True:
        usrin = input('input text to send to fifo')
        send.write(usrin)
