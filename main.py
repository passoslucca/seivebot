import telebot
import sqlite3



conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG2 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS COOPSTEC (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS PLATAFORMAG5 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG1 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG3 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG4 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG5 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS OTTRANSG6 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS PLATAFORMAG1 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS PLATAFORMAG2 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS PLATAFORMAG3 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS PLATAFORMAG4 (codigo_alphanumerico TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS COOPTACS (codigo_alphanumerico TEXT)''')



CHAVE_API = "6273188874:AAHM1CaJqtI_cNHbjtIb84UnmuMHvK8ooiI"

bot = telebot.TeleBot(CHAVE_API)






@bot.message_handler(commands=["COOPSTEC"])
def COOPSTEC(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_COOPSTEC)


def armazenar_COOPSTEC(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO COOPSTEC (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["COOPTACS"])
def COOPTACS(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_COOPTACS)


def armazenar_COOPTACS(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO COOPTACS (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAFORMAG1"])
def PLATAFORMAG1(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_PLATAFORMAG1)


def armazenar_PLATAFORMAG1(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PLATAFORMAG1 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


@bot.message_handler(commands=["PLATAFORMAG2"])
def PLATAFORMAG2(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_PLATAFORMAG2)


def armazenar_PLATAFORMAG2(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PLATAFORMAG2 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAFORMAG3"])
def PLATAFORMAG3(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_PLATAFORMAG3)


def armazenar_PLATAFORMAG3(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PLATAFORMAG3 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()



@bot.message_handler(commands=["PLATAFORMAG5"])
def PLATAFORMAG5(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_PLATAFORMAG5)


def armazenar_PLATAFORMAG5(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PLATAFORMAG5 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAFORMAG4"])
def PLATAFORMAG4(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_PLATAFORMAG4)


def armazenar_PLATAFORMAG4(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO PLATAFORMAG4 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG1"])
def OTTRANSG1(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG1)


def armazenar_OTTRANSG1(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG1 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG2"])
def OTTRANSG2(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG2)


def armazenar_OTTRANSG2(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG2 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG3"])
def OTTRANSG3(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG3)


def armazenar_OTTRANSG3(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG3 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG4"])
def OTTRANSG4(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG4)


def armazenar_OTTRANSG4(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG4 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG5"])
def OTTRANSG5(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG5)


def armazenar_OTTRANSG5(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG5 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OTTRANSG6"])
def OTTRANSG6(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro")
    bot.register_next_step_handler(mensagem, armazenar_OTTRANSG6)


def armazenar_OTTRANSG6(mensagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO OTTRANSG6 (codigo_alphanumerico) VALUES (?)", (codigo,))
            conn.commit()
            bot.send_message(mensagem.chat.id, "Carro enviado à garagem com sucesso.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


@bot.message_handler(commands=["0TTRANSG1"])
def consultar_OTTRANSG1(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG1")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG1 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG1.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG2"])
def consultar_OTTRANSG2(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG2")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG2 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG2.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG3"])
def consultar_OTTRANSG3(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG3")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG3 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG3.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG4"])
def consultar_OTTRANSG4(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG4")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG4 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG4.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG4"])
def consultar_OTTRANSG4(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG4")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG4 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG4.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG5"])
def consultar_OTTRANSG5(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG5")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG5 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG5.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["0TTRANSG6"])
def consultar_OTTRANSG6(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM OTTRANSG6")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem OTTRANSG6 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em OTTRANSG6.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["C00PSTEC"])
def consultar_COOPSTEC(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM COOPSTEC")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem COOPSTEC são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em COOPSTEC.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["C00PTACS"])
def consultar_COOPTACS(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM COOPTACS")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem COOPTACS são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em COOPTACS.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAF0RMAG1"])
def consultar_PLATAFORMAG1(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM PLATAFORMAG1")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem PLATAFORMAG1 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em PLATAFORMAG1.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAF0RMAG2"])
def consultar_PLATAFORMAG2(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM PLATAFORMAG2")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem PLATAFORMAG2 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em PLATAFORMAG2.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAF0RMAG3"])
def consultar_PLATAFORMAG3(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM PLATAFORMAG3")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem PLATAFORMAG3 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em PLATAFORMAG3.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAF0RMAG4"])
def consultar_PLATAFORMAG4(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM PLATAFORMAG4")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem PLATAFORMAG4 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em PLATAFORMAG4.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLATAF0RMAG5"])
def consultar_PLATAFORMAG5(mensagem):
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_alphanumerico FROM PLATAFORMAG5")
            resultados = cursor.fetchall()
            if resultados:
                codigos = [r[0] for r in resultados]
                bot.send_message(mensagem.chat.id, f"Os carros na garagem PLATAFORMAG5 são: {', '.join(codigos)}")
            else:
                bot.send_message(mensagem.chat.id, "Não há nenhum carro a disposição da vistoria em PLATAFORMAG5.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG1"])
def retirar_OTTRANSG1(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG1"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG2"])
def retirar_OTTRANSG2(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG2"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG3"])
def retirar_OTTRANSG3(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG3"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG4"])
def retirar_OTTRANSG4(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG4"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG5"])
def retirar_OTTRANSG5(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG5"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["OttRANSG6"])
def retirar_OTTRANSG6(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "OTTRANSG6"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


@bot.message_handler(commands=["COOPStEC"])
def retirar_COOPSTEC(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "COOPSTEC"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLAtAFORMAG1"])
def retirar_PLATAFORMAG1(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "PLATAFORMAG1"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLAtAFORMAG2"])
def retirar_PLATAFORMAG2(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "PLATAFORMAG2"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLAtAFORMAG3"])
def retirar_PLATAFORMAG3(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "PLATAFORMAG3"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLAtAFORMAG4"])
def retirar_PLATAFORMAG4(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "PLATAFORMAG4"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

@bot.message_handler(commands=["PLAtAFORMAG5"])
def retirar_PLATAFORMAG5(mensagem):
    bot.send_message(mensagem.chat.id, "Informe o número do alvará do carro que deseja retirar")
    bot.register_next_step_handler(mensagem, lambda msg: retirar_carro(msg, "PLATAFORMAG5"))

def retirar_carro(mensagem, garagem):
    codigo = mensagem.text
    try:
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"DELETE FROM {garagem} WHERE codigo_alphanumerico = ?", (codigo,))
                conn.commit()
                bot.send_message(mensagem.chat.id, "Carro retirado da garagem com sucesso.")
            else:
                bot.send_message(mensagem.chat.id, "Não foi encontrado nenhum carro com esse alvará na garagem.")
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
           Escolha uma garagem para consultar (Clique no item):
            /0TTRANSG1
            /0TTRANSG2
            /0TTRANSG3
            /0TTRANSG4
            /0TTRANSG5
            /0TTRANSG6
            /C00PSTEC
            /C00PTACS
            /PLATAF0RMAG1
            /PLATAF0RMAG2
            /PLATAF0RMAG3
            /PLATAF0RMAG4
            /PLATAF0RMAG5"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
               Escolha uma garagem colocar carro (Clique no item):
                /OTTRANSG1
                /OTTRANSG2
                /OTTRANSG3
                /OTTRANSG4
                /OTTRANSG5
                /OTTRANSG6
                /COOPSTEC
                /COOPTACS
                /PLATAFORMAG1
                /PLATAFORMAG2
                /PLATAFORMAG3
                /PLATAFORMAG4
                /PLATAFORMAG5"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
               Escolha uma garagem para retirar (Clique no item):
                /OttRANSG1
                /OttRANSG2
                /OttRANSG3
                /OttRANSG4
                /OttRANSG5
                /OttRANSG6
                /COOPStEC
                /COOPtACS
                /PLAtAFORMAG1
                /PLAtAFORMAG2
                /PLAtAFORMAG3
                /PLAtAFORMAG4
                /PLAtAFORMAG5"""
    bot.send_message(mensagem.chat.id, texto)




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
        Escolha uma opção para continuar (Clique no item):
         /opcao1 Consultar carros à disposição da vistoria
         /opcao2 Colocar um carro à disposição da vistoria
         /opcao3 Liberar carro após a vistoria
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling()
