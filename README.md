# Casebot

Casebot is a robotic legal assistant for Slack that looks up cases by citation. It's written in Python, and is licensed under the Affero GPLv3 open source license.

## How to Use Casebot

Casebot will respond to direct messages, or to @-messages if you add it to a channel. Your message to Casebot should include just a case citation.

For example, if you type `@casebot 410 U.S. 113`, Casebot will look up *Roe v. Wade* and give you a link to read the opinion on [CourtListener](https://www.courtlistener.com/).

## Limitations

Unfortunately, Casebot's legal education
was somewhat abbreviated, so (for now) it only knows how to look up cases by citation, like `410 U.S. 113`. For Casebot's purposes, a citation is broken into three parts:

* volume (the `410` part in the example above)
* reporter (`U.S.`)
* page (`113`)

## Installation

Casebot runs on your own computer. This can be your own desktop or laptop, or a server. You could probably get it to run on Windows, but so far it's been tested on Mac and Cygwin (a Linux-like environment for Windows).

1. If it's not already on your computer, install [Python](https://www.python.org/downloads/). Casebot has only been tested on Python 3, but it *should* also work on version 2. If you're using a Mac or Linux, you can skip this because Python should be preinstalled.

1. Create a Slack bot user at <https://my.slack.com/services/new/bot>. Make note of the API token you get.

1. Edit `run.sh` and paste in your new API token just after the equals sign on the first line, replacing `YOUR_BOT_API_TOKEN`:

  ```
  export SLACKBOT_API_TOKEN=YOUR_BOT_API_TOKEN
  ```

1. Install Python dependencies. In a terminal:

  ```shell
  pip install -r requirements.txt
  ```

1. In the same terminal, run `run.sh`:

  ```shell
  ./run.sh
  ```
1. You should see your bot come online in Slack. Send it a test message!
