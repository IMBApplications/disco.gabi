from disco.bot import Bot, Plugin

class Development(Plugin):
    # Listen to development commands
    @Plugin.command('pull')
    def on_pull_command(self, event):
        import git

        appRoot = os.path.dirname(os.path.abspath(__file__))
        g = git.cmd.Git(appRoot)

        try:
            ret = g.pull()
        except Exception as e:
            print(e)
            ret = str(e)

        event.msg.reply(ret)

    @Plugin.command('restart')
    def on_restart_command(self, event):
        import sys

        event.msg.reply('restarting...')
        sys.exit(0)
