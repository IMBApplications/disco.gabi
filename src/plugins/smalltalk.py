from disco.bot import Bot, Plugin


class Smalltalk(Plugin):
    # Plugins provide an easy interface for listening to Discord events
    @Plugin.listen('ChannelCreate')
    def on_channel_create(self, event):
        event.channel.send_message('Woah, a new channel huh!')

    # They also provide an easy-to-use command component
    @Plugin.command('ping')
    def on_ping_command(self, event):
        event.msg.reply('Pong!')

    # Which includes command argument parsing
    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)

    # React to channel
    # @Plugin.listen('MessageCreate')
    # def on_message(self, event):
    #     # self.log.info(u'{}: {}'.format(event.author, event.content))
    #     ret_message = ""
    #
    #     """Lets groove"""
    #     if len(args) > 0:
    #         self.send_simple_reply(mess, _('Groovy? Did i hear groovy? {0} is groovy!').format(args))
    #     else:
    #         self.send_simple_reply(mess, _('Groovy? Did i hear groovy? I am groovy!'))

    # if ret_message:
    #     event.channel.send_message(ret_message)
