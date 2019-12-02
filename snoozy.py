from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

    #####
    # DISCLAIMER:
    # this is a 1.0 for a tumblr meme so i did this shit the quickest way i
    # knew: remapped a makeymakey toy and stuck in on the clock so that
    # hitting the snooze button also completed a circuit and hit "a" +
    # enter on IDLE for me. sorry to anyone wanting good UI 
    #####

cont = True
c = 1
while cont:
    ques = str(input('snooze: '))
    if ques.lower() == "a":
        answer = "Disgusting little man slumbers on %s time(s)" %c
        twitter.update_status(status=answer)
        c=c+1
        
    #break by hitting stop on clock which just hits enter
    else:
        cont = False
        answer = "About fuckin time"
        twitter.update_status(status=answer)
        print('finally')
        exit
