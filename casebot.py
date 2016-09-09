from slackbot.bot import Bot


@listen_to('yo')
def yo(message):
    message.reply('Yo ho ho!')


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
