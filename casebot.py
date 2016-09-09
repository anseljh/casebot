from slackbot.bot import Bot
from slackbot import settings
from slackbot.bot import listen_to, respond_to


settings.DEFAULT_REPLY = "Eh?"


@respond_to("123 F.2d 456")
def handle_citation(message):
    message.reply("Full citation: Example v. Example, 123 F.2d 456 (9th Cir. 2000)")
    message.reply("CourtListener URL: https://stuff")


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
