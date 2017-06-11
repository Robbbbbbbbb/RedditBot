###################################################################
#
#                   RedditBot AutoMod Bot v0.1.3
#                         by /u/Robbbbbbbbb
#
#
#               https://github.com/Robbbbbbbbb/RedditBot
###################################################################

import praw
import time
import os

###################################################################
#  Start editing below this line
###################################################################
#  Define the keywords that the bot is looking for
keyword = ['keyword1', 'keyword2']
# Which Subreddit to use
sub = 'Test'
# Number of comments to parse through
numComments = 25
# How many seconds to sleep before running again
sleepTime = 10
# Name of the user account stored in praw.ini
userAccount = 'MyRedditAccount'
# Provide a short description of this program
userAgent = 'YOURPROJECTNAME via RedditBot AutoMod v0.1.2'
# Define comment being sent
REPLY_MESSAGE = 'I see you!'
#
###################################################################
#  End Editing
###################################################################
comments_replied_to = []


# method to call for authenticating account stored in praw.ini
def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit(userAccount, user_agent=userAgent)
    print('Authenticated as {}'.format(reddit.user.me()))

    return reddit


# method to call to create text list of comment IDs and read from it
def get_saved_comments():
    print('Making sure TXT list exists')
    if not os.path.isfile('comments_replied_to.txt'):
        print('WARNING: "comments_replied_to.txt" doesn\'t exist, creating.')
        comments_replied_to = []
    else:
        print('List exists, continuing...')
        with open('comments_replied_to.txt', 'r+') as f:
            print('Read TXT list')
            comments_replied_to = f.read()
            print('Split TXT list')
            comments_replied_to = comments_replied_to.split("\n")
    print('Return')

    return comments_replied_to


def main():
    comments_replied_to = get_saved_comments()
    print('Prepare auth function')
    reddit = authenticate()
    print('Start run_bot function loop')
    while True:
        print('begin run_bot function')
        run_bot(reddit, comments_replied_to)


def run_bot(reddit, comments_replied_to):
    print('Obtaining {}'.format(numComments) + ' comments')
    for comment in reddit.subreddit(sub).comments(limit=25):
        if any(keyword in comment.body.lower() for keyword in keywords):
            if comment.id not in comments_replied_to and not comment.author == reddit.user.me():
                try:
                    print('NEW string found in comment: ' + comment.id)
                    comment.reply(REPLY_MESSAGE)
                    print('Replied to ' + comment.id)
                    comments_replied_to.append(comment.id)
                    print('Open TXT list to write change')
                    with open('comments_replied_to.txt', 'a') as f:
                        print('Write comment ID to TXT list')
                        f.write(comment.id + '\n')
                except praw.exceptions.APIException as ErrorRateExceeded:
                    prawRateMessage = str(ErrorRateExceeded.message)
                    rateSplit = ''.join(filter(str.isdigit, prawRateMessage))
                    rateSplitNum = int(rateSplit)
                    print('WARNING: Rate limit exceeded. Sleeping for ' + rateSplit + ' minutes')
                    seconds = 60
                    apiSleep = rateSplitNum * seconds
                    time.sleep(apiSleep)
                    print('Resuming after Look completes!')
    print('Look done, sleeping.')
    # Sleep before running again
    time.sleep(sleepTime)

print('PROGRAM START. Calling main function')
if __name__ == '__main__':
    main()

print('prior to import: {}'.format(__name__))
from reddit_bot import run_bot
print('Preparing bot...')
