import sys
import json
import re

tf = {}

def cal_term_frq(tweet_file):
    tweets = open(tweet_file)
    total = 0
    for line in tweets:
        j = json.loads(line)
        if 'text' in j.keys(): #tweets
            text = j['text']
            for w in text.split(' '):
                w = w.lower()
                match = re.search('\w+',w)
                if match:
                    total += 1.0
                    w = match.group()
                    if not w in tf.keys():
                        tf[w]=0
                    tf[w]+=1
    for w in tf.keys():
        tf[w] = tf[w]/total
        
    tweets.close()
    #print total
      
def print_tf_out():
    for key in tf.keys():
        print key, tf[key]

        

def main():
    cal_term_frq(sys.argv[1])
    print_tf_out()

if __name__ == '__main__':
    main()
