# Limbo
### A [Slack](https://slack.com/) chatbot

![](https://travis-ci.org/llimllib/limbo.svg?branch=master)

## Installation

1. Clone the repo
2. `pip install -r requirements.txt`
3. [Create a bot user](https://my.slack.com/services/new/bot) if you don't have one yet, and copy the API Token
4. export SLACK_TOKEN="your-api-token"
5. make run (or make repl for local testing)
6. Invite Limbo into any channels you want it in, or just message it in #general. Try typing `!gif dubstep cat` to test it out

![kitten mittens](http://i.imgur.com/xhmD6QO.png)

## Commands

It's super easy to add your own commands! Just create a python file in the plugins directory with an `on_message` function that returns a string.

You can use the `!help` command to print out all available commands and a brief help message about them. `!help <plugin>` will return just the help for a particular plugin.

These are the current default plugins:

* [calc](https://github.com/llimllib/limbo#calc)
* [emoji](https://github.com/llimllib/limbo#emoji)
* [flip](https://github.com/llimllib/limbo#flip)
* [gif](https://github.com/llimllib/limbo#gif)
* [google](https://github.com/llimllib/limbo#google-or-search)
* [help](https://github.com/llimllib/limbo#help)
* [image](https://github.com/llimllib/limbo#image)
* [map](https://github.com/llimllib/limbo#map)
* [stock](https://github.com/llimllib/limbo#stock)
* [stockphoto](https://github.com/llimllib/limbo#stockphoto)
* [weather](https://github.com/llimllib/limbo#weather)
* [wiki](https://github.com/llimllib/limbo#wiki)
* [youtube](https://github.com/llimllib/limbo#youtube)

### calc

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/calc.png)

---

### emoji

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/emoji.png)

---

### flip

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/flip.png)

---

### gif

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/gif.png)

---

### google (or search)

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/google.png)

---

### help

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/help.png)

---

### image

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/image.png)

---

### map

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/map.png)

---

### stock

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/stock.png)

---

### stockphoto

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/stockphoto.png)

---

### weather

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/weather.png)

---

### wiki

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/wiki.png)

---

### youtube

![](https://raw.githubusercontent.com/llimllib/limbo/master/docs/youtube.png)

---

## Contributors

* [@fsalum](https://github.com/fsalum)
* [@rodvodka](https://github.com/rodvodka)
* [@mattfora](https://github.com/mattfora)
* [@dguido](https://github.com/dguido)
* [@JoeGermuska](https://github.com/JoeGermuska)
* [@MathyV](https://github.com/MathyV)
* [@stopspazzing](https://github.com/stopspazzing)
* [@noise](https://github.com/noise)
