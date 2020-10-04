import botogram
import sys
import utils
from objects import static
sys.path.append("..")


def start(chat, message):
    res = static.menu()
    chat.send(res['text'], attach=res['kb'])
    utils.register_user(message.sender.id)
