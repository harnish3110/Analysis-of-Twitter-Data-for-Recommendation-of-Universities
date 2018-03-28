import unicodedata2 as unicodedata
import json
import tweepy

auth = tweepy.OAuthHandler('PjYAex5Do7e4ldslfFqj8rcmB', 'MHrbXAukQ5wYgyXM9QWX4qys19uzHFo7gL9V3VqKYxJFSWDgK0')
auth.set_access_token('84782380-zFrkL16EB71T0gkdQVieyYNa74zIt2brnbom1y2P1',
                      'OsWIkDSET0CefBnMgHRRdYKuxezPZEqr7v9r0vPrH7fay')
api = tweepy.API(auth)
tweets = []
def retrieve_tweets():
    global tweets
    tweets = api.search('university OR college OR undergraduate OR graduate OR masters', count=100,  result_type='recent')
    print 'Retrieving Started'
    file = open('data.txt', 'w')
    i = 0
    for tweet in tweets:
        i += 1
        # print tweet
        file.write(str(tweet))
        file.write("\n")
    file.close()
    print 'Retrieving Tweets Completed'

def save_tweets():
    print 'Saving Tweets'
    # print tweets
    file_tweets = open('../data_set/new_tweets.txt','a+')
    lastline = file_tweets.readlines()[-1].split(',')
    line_number = int(lastline[0])
    print 'Last line', lastline
    print 'Last line number', line_number
    for tweet in tweets:
        line_number+=1
        data = unicodedata.normalize('NFKD', tweet.text).encode('utf-8', 'ignore')
        file_tweets.write(str(line_number) + ', ,')
        file_tweets.write(json.dumps(data))
        file_tweets.write('\n')

    file_tweets.close()


def main():
    retrieve_tweets()
    save_tweets()

if __name__ == '__main__':
    main()

