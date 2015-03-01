To allow bot to read trello API:

Call this URL from Python API:

trello.get_token_url('unAdventure', expires='30days', write_access=True)

This will return a URL like:

https://trello.com/1/authorize?key=0d5c42401f53ce4f78210ab0a1b927fc&name=unAdventure&expiration=30days&response_type=token&scope=read,write'

Visit this in your browser whilst logged into the Trello account which you want to authorise unAdventure to use to access Trello.

When finished, this will return a key, like:

3ccccb1cfc411ac77022d83975b301b0ff597b150ee877c138ca43c4ee893d53

Call trello.set_token('key'), replacing key with this key.


