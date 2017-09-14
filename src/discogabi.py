import argparse
import os
import logging
from disco.client import Client, ClientConfig
from disco.bot import Bot, BotConfig
from disco.util.token import is_valid_token
from disco.util.logging import setup_logging


def disco_gabi():
    args = parse_arguments()

    if os.path.exists(args.config):
        config = ClientConfig.from_file(args.config)
    else:
        config = ClientConfig()

    if not is_valid_token(config.token):
        print('Invalid token passed')
        return

    setup_logging(level=getattr(logging, config.log_level.upper()))

    client = Client(config)

    bot_config = BotConfig(config.bot) if hasattr(config, 'bot') else BotConfig()
    if not hasattr(bot_config, 'plugins'):
        bot_config.plugins = args.plugin
    else:
        bot_config.plugins += args.plugin

    bot = Bot(client, bot_config)
    bot.run_forever()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Configuration file', default='config.json')
    parser.add_argument('--plugin', help='load plugins into the bot', nargs='*', default=[])
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    disco_gabi()