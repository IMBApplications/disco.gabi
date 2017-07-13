from disco.bot import Plugin
from datetime import datetime


class Birthdays(Plugin):
    def load(self, ctx):
        super(Birthdays, self).load(ctx)
        self.birthdays = self.storage.guild('birthdays')
        self.members = {}

    @Plugin.command('add', '<user:user> <value:str...>')
    def on_add(self, event, user, value):
        # check if value is a date

        try:
            datetime_object = datetime.strptime(value, '%d.%m.%Y')
        except TypeError:
            return event.msg.reply('Ehh Datum? (dd.mm.yyyy)')

        # check if user id is known
        if user.id in self.birthdays:
            return event.msg.reply('Weiss ich, weiss ich!')

        self.birthdays[user.id] = {
            "day": datetime_object.day,
            "month": datetime_object.month,
            "year": datetime_object.year
        }

        return event.msg.reply(u':ok_hand: den Geburstag von {} merk ich mir'.format(user.username, sanitize=True))

    @Plugin.command('list')
    def on_list(self, event):
        ret = []
        for user in self.birthdays.keys():
            for check_user in event.guild.members:
                if int(user) == check_user:
                    name = event.guild.members[check_user].user.username
                    break
            ret.append(name + ": %(day)s.%(month)s.%(year)s" % self.birthdays[user])

        return event.msg.reply("\n".join(ret), sanitize=True)

    @Plugin.command('delete', '<name:str>', aliases=['del', 'rmv', 'remove'])
    def on_tags_delete(self, event, name):
        if name not in self.birthdays:
            return event.msg.reply('That tag does not exist!')

        return event.msg.reply(u':ok_hand: I deleted the {} tag for you'.format(
            name
        ), sanitize=True)
