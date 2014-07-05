import sys
import json
import re
scores = {}

def load_dict(sent_file):
    afinnfile = open(sent_file,'r')
    for line in afinnfile:
        (term, score) = line.split('\t')
        scores[term]=int(score)
    afinnfile.close()

def cal_score(tweet_file):
    tf = open(tweet_file,'r')
    for line in tf:
        score = 0
	j = json.loads(line)
	if 'text' in j.keys():  #tweets
            text = j['text']
            print(text)
            for w in text.split(' '):
                w = w.lower()
                match = re.search('\w+',w)
                if match:
                    w = match.group()
                    print(w)
                    if w in scores.keys():
                        score+=scores[w]
            print(score)
    tf.close()

def main():
    load_dict(sys.argv[1])
    cal_score(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
