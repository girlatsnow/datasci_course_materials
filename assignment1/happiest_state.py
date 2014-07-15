import sys
import json
import re
scores = {}
state = {}
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
        
        stt = j['user']['location']
        if stt.find(',')==-1:
            continue
        else:
            stt = stt.split(',')[1].strip()
            if len(stt)==2:
                if not stt in state.keys():
                    state[stt]=0
                if 'text' in j.keys():  #tweets
                    text = j['text']
            
                    for w in text.split(' '):
                        w = w.lower()
                        match = re.search('\w+',w)
                        if match:
                            w = match.group()
                       
                            if w in scores.keys():
                                score+=scores[w]

                state[stt]+=score  

            
    tf.close()

def print_happiest_state():
    h = 0
    stt = ''
    for key in state.keys():
        if state[key]>=h:
            stt = key
    print stt       


def main():
    load_dict(sys.argv[1])
    cal_score(sys.argv[2])
    print_happiest_state()
   
if __name__ == '__main__':
    main()
