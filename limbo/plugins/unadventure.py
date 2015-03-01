"""!help [<command>] prints help on all commands if no command given, or a specific command"""

import re
import os
from strop import split

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!look( .*)?", text)
    if not match:
        return

    return "\nYou are standing outside a stone building. You can see a huge valley to your left. In front of you are two green doors. There is a note on the door"
