import re

myInventory = ["12 Blankets", "Book of Mistakes"]

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!inventory( )?(.*)?", text)
    if match:
        words = match[0][1].split(" ")
        if words[0] == 'add':
            myInventory.append(" ".join(words[1:]))
        if words[0] == 'remove':
            myInventory.remove(" ".join(words[1:]))
        return "\nIn your inventory is: \n   " + "\n   ".join(myInventory)
