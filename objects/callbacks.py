import botogram


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
            "Il bot è stato scritto da @Doppio. Contattalo per qualsiasi altra"
            "domanda, oppure premi il pulsante qui sotto per inviargli"
            "un messaggio."
        )
    message.edit(text, attach=kb, preview=False)
