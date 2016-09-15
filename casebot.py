from slackbot.bot import Bot
from slackbot import settings
from slackbot.bot import listen_to, respond_to
from string import Template
import requests
from pprint import pprint
import click
import configparser

settings.DEFAULT_REPLY = "Does not compute."
CL_URL_TEMPLATE = Template("https://www.courtlistener.com/c/$reporter/$volume/$page/")
MINIMUM_VIABLE_CITATION_PATTERN = r"^(\d+)\s([A-Za-z0-9.\s]+)\s(\d+)$"
config = {}


@respond_to(MINIMUM_VIABLE_CITATION_PATTERN)
def handle_citation(message, volume=None, reporter=None, page=None):
    global config
    # Look up using CourtListener /c tool
    mapping = {'volume': volume, 'reporter': reporter, 'page': page}
    url = CL_URL_TEMPLATE.substitute(mapping)
    request_headers = {'user-agent': config['General']['user_agent']}
    response = requests.get(url, headers=request_headers)

    # Give some output on stdout
    print(response)
    pprint(response.headers)
    print(response.url)

    # Send the message!
    if response.status_code == 404:
        message.reply("Sorry, I can't find that citation in CourtListener.")
    else:
        message.reply(response.url)


def build_config(ini):
    config = {}
    for section in ini.sections():
        if section not in config:
            config[section] = {}
        for pair in ini.items(section):
            config[section][pair[0]] = pair[1]
    return config


def set_setting(config, ini, section, option, passed_option=None):
    if section not in config:
        config[section] = {}
    if passed_option is not None:
        config[section][option] = passed_option
    else:
        config[section][option] = ini[section][option]
    return config


@click.command()
@click.option('config_file', '--config', type=click.File('r'), help="Configuation file", default='settings.ini')
@click.option('slack_token', '--slack-token', envvar='SLACKBOT_API_TOKEN', help="Slack bot token")
@click.option('courtlistener_token', '--courtlistener-token', envvar='COURTLISTENER_API_TOKEN', default=None, help="CourtListener API token (optional)")
def configure(config_file, slack_token, courtlistener_token):
    """
    Read configuration from settings.ini (or other file if specified)
    """
    global config

    # Read the .ini file
    ini = configparser.ConfigParser()
    ini.read_file(config_file)
    assert ini.has_section('Slack'), "Config file missing Slack section"
    assert ini.has_option('Slack', 'slack_token'), "Slack bot token missing from config file"

    # Build config dict from .ini file
    config = build_config(ini)

    # Update config dict with CLI parameters (overriding .ini settings)
    config = set_setting(config, ini, 'Slack', 'slack_token', slack_token)
    config = set_setting(config, ini, 'CourtListener', 'courtlistener_token', courtlistener_token)

    # Configure Slackbot settings
    # e.g., like https://github.com/lins05/slackbot/blob/03c73a19190ccea889540d935738509324e0c7d9/slackbot/bot.py#L21
    settings.API_TOKEN = config['Slack']['slack_token']
    settings.BOT_EMOJI = config['Slack']['bot_emoji']

    print("Settings:")
    pprint(config)

    # Done configuring. Run the bot!
    run_bot()


def run_bot():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    configure()
