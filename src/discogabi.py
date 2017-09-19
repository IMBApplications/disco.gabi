import argparse

from src.gabi.hate import *
from src.gabi.fun import *

from gevent import monkey

monkey.patch_all()


def disco_gabi():
    args = parse_arguments()

    from src.disco_util.disco_listener import start_disco_listener

    start_disco_listener(args, [ShitCommand(), AidsCommand(), SihCommand(), GroovyCommand(), RollCommand(), ImbaCommand()])


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='Configuration file', default='config.json')
    parser.add_argument('--plugin', help='load plugins into the bot', nargs='*', default=[])
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    disco_gabi()
