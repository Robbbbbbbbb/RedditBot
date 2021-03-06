# RedditBot
Simple single-function Reddit auto-mod bot written in Python 3. Based on the original code writen by /u/busterroni and the improvements by PRAW developer /u/bboe.

I'm not a fantastic Python developer, so there are probably some 'not-best-practice' things in here. I'll work on improving it as I learn, but this should at least get you going enough to automod a sub.

<strong>Prerequisites</strong>:
<ul>
<li>Python 3.6+</li>
<li><a href=https://github.com/praw-dev/praw>Python Reddit API Wrapper (PRAW)</a>, run "pip install praw"</li>
<li>A new <a href=https://ssl.reddit.com/prefs/apps/>Reddit Application</a></li>
</ul>

<strong>Current version</strong>: v0.1.3 (Release 06/11/2017)

All of your variables should be in the header, but you will also need to edit praw.ini with the user account details generated from the Reddit app.

<strong>Planned (future) improvements</strong>:
<ul>
<li><s>Support for multiple keywords using lists</s> - done in v0.1.2</li>
<li><s>Error handling for exceeded rate limits</s> - done in v0.1.3</li>
<li>Performance handling for large amounts of comments by utilizing SQL lite instead of a TXT file for comments</li>
<li>Allow bot to listen for keyword lists and reply with different REPLY_MESSAGE</li>
<li>Integrate support for multiple user accounts to allow for more than one bot to post from a single instance of this program</li>
</ul>
