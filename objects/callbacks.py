import botogram
from objects import static
import config
import sqlite3
import utils

conn = sqlite3.connect(config.DATABASE_FILE_NAME + '.db')
c = conn.cursor()

def menu(query, message, lang):
    query.notify("👌🏻 Ok!")
    res = static.menu()
    message.edit(res['text'], attach=res['kb'], preview=False)


def informazioni(query, message, lang):
    query.notify("👌🏻 Ok!")
    if lang == "it":
        kb = botogram.Buttons()
        kb[0].callback("📬 Invia un messaggio", "contact")
        kb[1].callback("🔙 Torna indietro", "menu")
        text = (
            "ℹ️ <b>Informazioni sul bot</b>\n\n"
            "Il bot è scritto in linguaggio <b>Python 3</b>, utilizza un database"
            "<b>SQLite</b> e risiede su una <b>VPS Linux</b>.\n"
            "Se sei interessato a visualizzare il codice sorgente puoi farlo "
            "<a href='github.com/MattiaEffendi/Marks'>qui</a>.\n"
            "Il bot è stato scritto da @Doppio. Contattalo per qualsiasi altra "
            "domanda, oppure premi il pulsante qui sotto per inviargli "
            "un messaggio."
        )
    message.edit(text, attach=kb, preview=False)

def libretto(query, message, lang):
    query.notify("👌🏻 Ok!")
    kb = botogram.Buttons()
    kb[0].callback("📝 Aggiungi un voto", "add_mark")
    kb[1].callback("🔙 Torna indietro", "menu")
    c.execute("SELECT COUNT(ID), AVG(Mark) FROM Voti WHERE IDU = ?", (int(query.sender.id),))
    res = c.fetchone()
    text = (
        "Al momento hai <b>" + str(res[0]) + "</b> voti. \n\n"
        "La tua media è <b>" + str(res[1]) + "</b>."
    )
    message.edit(text, attach=kb, preview=False)

def add_mark(query, message, lang):
    query.notify("👌🏻 Ok!")
    utils.set_user_state(int(query.sender.id), 'aggiungi_voto')
    text = "Invia il voto nel prossimo messaggio"
    message.edit(text, preview=False)
