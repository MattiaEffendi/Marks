import botogram
import sqlite3
import config, utils
from objects import messages, callbacks, commands

conn = sqlite3.connect(config.DATABASE_FILE_NAME + '.db')
c = conn.cursor()
bot = botogram.create(config.API_TOKEN)

if config.FIRST_START:
    utils.first_start()


@bot.command("start")
def start(chat, message):
    commands.start(chat)


@bot.callback("informazioni")
def informazioni(query, message):
    callbacks.informazioni(query, message, "it")


bot._components[0]._Component__no_commands = []
bot._main_component._add_no_commands_hook(messages.command_not_found)
if __name__ == '__main__':
    bot.run()
