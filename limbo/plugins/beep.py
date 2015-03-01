
import re
import os

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!beep( .*)?", text)
    if match:
        os.system('play --no-show-progress --null --channels 1 synth 0.1 sine 1000')
        return "\nSomewhere, I beeped"

