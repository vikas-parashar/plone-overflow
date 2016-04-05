
# plone-overflow
Slack bot to watch stack overflow for new questions with 'plone' tag and post them in channel.

![watching 'javascript' tag and posting questions](http://i.imgur.com/Z06N8kA.png "watching 'javascript' tag and posting questions")


## Installation
Clone the repo:

  `git clone https://github.com/vikas-parashar/plone-overflow.git`

Install requirements:

  `pip install -r requirements.txt`

Set Environment variables:

  SLACK_PUSH_URL(get it from [here](https://api.slack.com/incoming-webhooks))

  STACKEXCHANGE_API_KEY(get it from [here](http://stackapps.com/apps/oauth/register))

Now, create a cron job to check frquently, and you'are done!
