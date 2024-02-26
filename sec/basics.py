# proof of concept type stuff and review, examples etc...
import sys
import socket
from datetime import datetime
# AFI NET, socket stream, 
# https://www.youtube.com/watch?v=WnN6dbos5u8&t=8567s

# List and Dictionaries

movies = ["Seven Samurai", "The Shining", "Dumb and Dumber", "Gladiator"]
person = ["Wednesday", "Angelica", "Beau", "Frank"]
combined = zip(movies, person)

# this seems useful

movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)


# port scanner

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 SOCK_STREAM = port
        # target = 
        socket.setdefaulttimeout(1) # is a float
        result = s.connect_ex((target.port)) # returns error indicator
        print("checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))

        s.close()
except KeyboardInterrupt:
    print('\nexited out')
    sys.exit()


except socket.gaierror:
    print('\nhost name could not be resolved')
    sys.exit()


except socket.error:
    print('\ncouldn\'t connect to server')
    sys.exit()

# ctrl - o is my new favorite friend

#########################################################################################################################
sys.exit()

