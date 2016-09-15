# Casebot

Casebot is a robotic legal assistant for Slack that looks up cases by citation. It's written in Python, and is licensed under the Affero GPLv3 open source license.

## How to Use Casebot

Casebot will respond to direct messages, or to @-messages if you add it to a channel. Your message to Casebot should include just a case citation, or `find` and the name of a case (or part of it).

### Examples

* If you type `@casebot 410 U.S. 113`, Casebot will look up *Roe v. Wade* from its citation, and will give you a link to read the opinion on [CourtListener](https://www.courtlistener.com/).
* If you type `@casebot find brown v. board`, Casebot will search CourtListener and find the landmark 1954 Supreme Court case *Brown v. Board of Education*.

## Limitations

Unfortunately, Casebot's legal education
was somewhat abbreviated, so its citation lookup is fairly rigid. Casebot only knows how to look up well-formed citations, like `410 U.S. 113`. For Casebot's purposes, a citation is broken into three parts:

* volume (the `410` part in the example above)
* reporter (`U.S.`)
* page (`113`)

Reporters are also case-sensitive: `U.S.` will work, but `u.s.` will not. Don't worry, a fix is in the works.

When using `find`, Casebot only returns the first result. It may not be what you were looking for!

## Installation

Casebot runs on your own computer. This can be your own desktop or laptop, or a server. You could probably get it to run on Windows, but so far it's been tested on Mac and [Cygwin](https://cygwin.com/) (a Linux-like environment for Windows).

1. *If it's not already on your computer*, install [Python](https://www.python.org/downloads/). Casebot was developed in Python 3, but it *should* also work on Python 2. If you're using a Mac, Linux, or Cygwin, you can skip this step because Python should already be installed.

1. Create a Slack bot user at <https://my.slack.com/services/new/bot>. Write down the API token you get.

1. Edit the `settings.ini` file and paste in your new API token after the equals sign on the line that starts with `slack_token`:

  ```
  slack_token=YOUR_BOT_API_TOKEN
  ```

1. Install the Python packages that Casebot needs. In a terminal:

  ```shell
  pip3 install -r requirements.txt
  ```

1. In the same terminal, run the program, using Python:

  ```shell
  python3 casebot.py
  ```
1. You should see your bot come online in Slack. Send it a test message!
