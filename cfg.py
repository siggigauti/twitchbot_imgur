# cfg.py
HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "linkcatcher_bot"            # your Twitch username, lowercase
PASS = "oauth:tyb6k1ve8unugkarx7x389q7qa0q9x" # your Twitch OAuth token
CHAN = "#timthetatman"                   # the channel you want to join

RATE = (20/30) # messages per second

PATT = [
    r"swear"
]