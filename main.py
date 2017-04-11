# bot.py
import cfg
import socket
import re
import time

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


# network functions go here
try:
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))
    connected = True
except Exception as e:
    print(str(e))
    connected = False

def main_loop():
    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            try:
                username = re.search(r"\w+", response).group(0) # return the entire match
                message = CHAT_MSG.sub("", response)
                #Might be able to use list. i.e. mylist = list(message.split())
                #Each 'word' get its own spot in the list
                #then check if imgur is in any of the 'words'

                print(username + ": " + message)
                if "imgur.com" in message:

                    m = re.search('imgur.com/(.+?)( |$)', message)
                    if m:
                        f = open('imgurlinks.txt', 'a')
                        f.write('imgur.com/'+m.group(1)+'\n')
                        f.close()
                   
                #for pattern in cfg.PATT:
                 #   if re.match(pattern, message):
                  #      ban(s, username)
                   #     break
            except UnicodeEncodeError:
                continue
        time.sleep(0.0001)

if __name__ == '__main__':
    main_loop()

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(sock, ".timeout {}".format(user, secs))