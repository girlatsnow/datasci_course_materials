import sys
import json
import re

scores = {}
scores_out = {}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def load_dict(sent_file):
    sents = open(sent_file)
    for line in sents:
        (term, score) = line.split('\t')
        scores[term]=int(score)
    sents.close()

def cal_term_sent(tweet_file):
    tweets = open(tweet_file)
    for line in tweets:
        j = json.loads(line)
        if 'text' in j.keys(): #tweets
            text = j['text']
            tweets_in = []
            tweets_out = []
            score_in = 0
            for w in text.split(' '):
                w = w.lower()
                match = re.search('\w+',w)
                if match:
                    w = match.group()
                    if w in scores.keys():
                        score_in += scores[w]
                    else:
                        tweets_out.append(w)
            
            for w in tweets_out:
                if not w in scores_out.keys():
                    scores_out[w]=0
                scores_out[w]+= score_in
    tweets.close()
      
def print_score_out():
    for key in scores_out.keys():
        print key, scores_out[key]

        

def main():
    load_dict(sys.argv[1])
    cal_term_sent(sys.argv[2])
    print_score_out()

if __name__ == '__main__':
    main()
