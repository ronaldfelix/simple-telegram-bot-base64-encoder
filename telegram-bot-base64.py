from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import base64

def start(update, context):
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Hola manda tu mensaje y te lo delvolveré codificado en base64 😎😎😎"
    )
start_handler = CommandHandler("start", start)

def codificar_base64(cadena):
    cadena_codificada = base64.b64encode(cadena.encode('utf-8')).decode('utf-8')
    return cadena_codificada

def echo(update, context):
    respuesta = update.message.text
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = codificar_base64(respuesta)
    )
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

if __name__ == "__main__":
    updater = Updater(token="REPLACE-WITH-YOUR-TELEGRAM-BOT-TOKEN")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()