import sys
import json
import re

hashtag = {}

def count_hashtag(tweet_file):
    tweets = open(tweet_file)
    total = 0
    for line in tweets:
        j = json.loads(line)
        if 'text' in j.keys(): #tweets
            hashtags = j['entities']['hashtags']
            for ht in hashtags:
                if 'text' in ht.keys():    #hashtags
                    if not ht['text'] in hashtag.keys():
                        hashtag[ht['text']]=0
                    hashtag[ht['text']]+=1
        
    tweets.close()
    #print total
      
def print_hashtag_out():
    l = sorted(hashtag.items(), key=lambda d:d[1])
    for ht in l[:10]:
        print ht[0],ht[1]
        

def main():
    count_hashtag(sys.argv[1])
    print_hashtag_out()

if __name__ == '__main__':
    main()
