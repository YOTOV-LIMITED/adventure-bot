"""!help [<command>] prints help on all commands if no command given, or a specific command"""

import re

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!look( .*)?", text)
    if not match:
        return

    helptopic = match[0].strip()
    if helptopic:
        return server.hooks["help"].get(helptopic, "No help found for {0}".format(helptopic))
    else:
        return "\nYou are standing outside a stone building. You can see a huge valley to your left. In front of you are two green doors. There is a note on the door"
