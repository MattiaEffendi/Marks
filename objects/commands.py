import botogram
import sys
import utils
sys.path.append("..")


def start(chat, message):
    kb = botogram.Buttons()
    kb[0].callback("📚 Apri il tuo libretto", "libretto")
    kb[1].callback("🔧 Impostazioni", "impostazioni")
    kb[1].callback("ℹ️ Informazioni", "informazioni")
    text = (
        "📝 <b>Benvenuto in iMarks!</b>\n\n"
        "In questo bot potrai salvare tutti i tuoi voti, calcolare i voti che"
        "ti servono per raggiungere le medie che desideri, e creare obiettivi"
        "e promemoria.\n\n"
        "<i>Seleziona un'opzione dal menu.</i>"
    )
    chat.send(text, attach=kb)
    utils.register_user(message.sender.id)


