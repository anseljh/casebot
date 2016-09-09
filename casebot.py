from slackbot.bot import Bot
from slackbot import settings
from slackbot.bot import listen_to, respond_to
from string import Template
import requests
from pprint import pprint


settings.DEFAULT_REPLY = "Eh?"
CL_URL_TEMPLATE = Template("https://www.courtlistener.com/c/$reporter/$volume/$page/")
MINIMUM_VIABLE_CITATION_PATTERN = r"^(\d+)\s([A-Za-z0-9.\s]+)\s(\d+)$"
USER_AGENT_STRING = "casebot https://github.com/anseljh/casebot"


@respond_to(MINIMUM_VIABLE_CITATION_PATTERN)
def handle_citation(message, volume=None, reporter=None, page=None):
    # Look up using CourtListener /c tool
    mapping = {'volume': volume, 'reporter': reporter, 'page': page}
    url = CL_URL_TEMPLATE.substitute(mapping)
    request_headers = {'user-agent': USER_AGENT_STRING}
    response = requests.get(url, headers=request_headers)

    # Give some output on stdout
    print(response.status_code)
    pprint(response.headers)
    print(response.url)
    print(response)

    # Send the message!
    if response.status_code == 404:
        message.reply("Sorry, I can't find that citation in CourtListener.")
    else:
        message.reply(response.url)


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
