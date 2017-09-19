def user_targetet_reply(with_user_text, without_user_text, msg):
    if len(msg.msg) > 0:
        response = with_user_text.format(msg.msg)
    else:
        response = without_user_text
    msg.reply(response)
