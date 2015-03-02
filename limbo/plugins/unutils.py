import re
import yaml
import inflection

myInventory = {}

def on_message(msg, server):
	text = msg.get("text", "")
	match = re.findall(r"!inventory( )?(.*)?", text)
	if match:
		words = match[0][1].split(" ")

		if words[0] == 'add':
			if words[1].isdigit():
				item = (" ".join(words[2:]))
				quantity = int(words[1])
			else:
				item = (" ".join(words[1:]))
				quantity = 1

			myInventory[inflection.singularize(item)] = quantity

		if words[0] == 'remove':
			if words[1].isdigit():
				item = (" ".join(words[2:]))
				quantity = int(words[1])
			else:
				item = (" ".join(words[1:]))
				quantity = 1

			myInventory[inflection.singularize(item)] -= quantity
			
			if myInventory[inflection.singularize(item)] == 0:
				del myInventory[inflection.singularize(item)]

		if words[0] == 'dump':
			myInventory.clear()
			return "\nYou have dumped all of your inventory."

		if words[0] == 'length':
			if len(myInventory) == 0:
				return "\nYou have nothing in your inventory."
			else:
				return "\nIn your inventory there are %d things." % len(myInventory)
		
	return "\nIn your inventory is: \n " + yaml.safe_dump(myInventory)