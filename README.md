# Skrypnyk-discord-spamer-bot
Skrypnyk - is a discord bot that can spam text or photos a specified number or countless times

# iNSTALL
git clone https://github.com/CoderBogdasha/Skrypnyk-discord-spamer-bot/

cd Skrypnyk-discord-spamer-bot/

pip install -r requirements.txt

python bot.py

# iNSTUCTION
use command:

* /spam argument1 argument2 ... - to spam text

argument1 - is the number of messages that will be sent by the bot (0 is infinity)

argument2 - is first word in messages(use ^long to send multilines messages)(use image_url to send a image(... is none))

... - is the rest words of the message

Example1: /spam 69 Artem homosexualist

Example2: /spam 8 https://cdn.discordapp.com/avatars/428159463002734595/efae82bb3a59509d27eb222fe91713a0.png

Example3: /spam 600000 ^long SAS

Note:
     To stop sending messages indefinitely, use: /spam stop

# SETTINGS in config.py

TOKEN - this is a discord token of your bot

bot_activity - this is the text that will be displayed as a status (Playing #####)

prefix - this is discord command prefix

way - is the path to the file where the settings will be saved(example: SAS.SAS)
