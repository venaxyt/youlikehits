# Made by @venaxyt on Github
import requests, gratient, random, string
from os import system

# Data
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

headers = {
	"Cookie": "YOUR COOKIES",
	}

# Retrieving all tweets ID from Retwets page request
tweet_id_list = []
tweet_id_number = 0
tweets = requests.get("https://www.youlikehits.com/retweets.php", headers=headers)
for tweet_number in (range(len((tweets.text).split('id="card')))):
    if not tweet_number == 0:
        characters = 0
        for character in ((tweets.text).split('id="card')[tweet_number]):
            characters += 1
        tweetid = ((tweets.text).split('id="card')[tweet_number])[:-(characters-6)]
        tweet_id_list.append(tweetid)
        tweet_id_number += 1

# Retrieving LBSESSIONID from response cookies
session_id = ((str(tweets.cookies)).split("LBSESSIONID=")[1]).replace(" for www.youlikehits.com/>]>", "")
idchar = session_id[6:][:-6]
idchar_position = alphabet.index(idchar); print('position : ' + str(idchar_position))
advanced_session_id = f"{(session_id[:-7] + alphabet[idchar_position + 2] + session_id[7:])}"
print(gratient.blue(f" [ADVANCED SESSION ID] {advanced_session_id}"))

headers = {
	"Cookie": f"YOUR COOKIES HERE; LBSESSIONID={session_id}; YOUR UTBM",
	}

print(gratient.purple(f" [RETRIVED TWEET NUMBER] : {tweet_id_number} / SESSION ID : {session_id}\n [ELAPSED] SECONDS : {str(tweets.elapsed).replace('0:00:0', '')}"))


# Requesting to get points for each retweet
for retweet_id in tweet_id_list:

    # Random value needed to send the request
    randomval = ''.join(random.choice(string.digits) for _ in range(16))

    # Extracting hidden value from retweet render request
    retweetrender = requests.get(f"https://www.youlikehits.com/retweetrender.php?id={retweet_id}", params = {"id": f"{retweet_id}"})
    characters = 0
    for character in ((retweetrender.text).split(retweet_id)[1])[2:]:
        characters += 1
    hidden = ((retweetrender.text).split(retweet_id)[1])[2:][:-(characters-32)]
    print(gratient.purple(f" [HIDDEN / ID] {hidden} / {retweet_id}"), end = "")
    
    # Custom parameters payload
    payload = {
        "id": retweet_id,
        "hidden": hidden,
        "step": "points",
        "rand": f"0.{randomval}",
        }

    retweet = requests.get(f"https://www.youlikehits.com/retweeted.php?id={retweet_id}&hidden={hidden}&step=points&rand=0.{randomval}", headers = headers, params = payload)
    print(gratient.purple(f" [>] RETWEETED DONE : {retweet_id}\n [RESPONSE] STATUS CODE : {retweet.status_code}\n [RESPONSE] TEXT : {retweet.text}\n [COOKIE] LBSESSIONID : {retweet.cookies}"))
