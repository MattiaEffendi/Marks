import config
import sqlite3
import botogram
import utils

conn = sqlite3.connect(config.DATABASE_FILE_NAME + '.db')
c = conn.cursor()

def command_not_found(chat, message):
    pass

def aggiungi_voto(chat, message, matches):
    c.execute("SELECT COUNT(IDU) FROM Utenti WHERE ID = ? AND State = 'aggiungi_voto'", (int(message.sender.id),))
    res = c.fetchone()
    if (res[0] != 1):
        return
    mark = float(message.text.replace(',', '.'))
    if (mark < 1 or mark > 10):
        chat.send('Il voto inserito non è valido!')
        return
    kb = botogram.Buttons()
    kb[0].callback("📚 Apri il tuo libretto", "libretto")
    c.execute("INSERT INTO Voti (IDU, Mark) VALUES (?, ?)", (int(message.sender.id), mark))
    utils.set_user_state(int(message.sender.id), '-')
    chat.send('Voto aggiunto!', attach=kb, preview=False)
