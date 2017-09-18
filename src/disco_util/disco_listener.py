import logging
import os

from disco.bot import Plugin, BotConfig, Bot
from disco.client import Client, ClientConfig
from disco.util.logging import setup_logging

from src.gabi.core import ChatMessage, ChatCommand


def start_disco_listener(args, commands):

    config = setup_config(args)
    setup_logging(level=getattr(logging, config.log_level.upper()))

    client = Client(config)

    bot, bot_config = setup_bot(args, client, config)

    chat_commands_plugin = Plugin(bot, bot_config)

    register_chat_commands(chat_commands_plugin, commands)

    bot.add_plugin(chat_commands_plugin)

    (bot or client).run_forever()


def register_chat_commands(chat_commands_plugin, commands: [ChatCommand]):
    for command in commands:
        register_chat_command(chat_commands_plugin, command)


def register_chat_command(chat_commands_plugin, command: ChatCommand):
    def chat_command_callback(event):
        content = event.msg.content.partition(' ')[2]
        msg = ChatMessage(content, event.msg.author.username, event.msg.reply)
        command.on_execute(msg)

    chat_commands_plugin.register_command(chat_command_callback, command.command_name)


def setup_bot(args, client, config):
    bot_config = BotConfig(config.bot) if hasattr(config, 'bot') else BotConfig()
    if not hasattr(bot_config, 'plugins'):
        bot_config.plugins = args.plugin
    else:
        bot_config.plugins += args.plugin

    bot_config.commands_require_mention = False

    bot = Bot(client, bot_config)
    return bot, bot_config


def setup_config(args):
    if os.path.exists(args.config):
        config = ClientConfig.from_file(args.config)
    else:
        config = ClientConfig()
    return config
