import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ChannelPostHandler, filters, ContextTypes
import nest_asyncio

# Función para manejar mensajes en grupos o privados
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"El ID de este grupo o chat privado es: {chat_id}")

# Función para manejar mensajes publicados en canales
async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.channel_post.reply_text(f"El ID de este canal es: {chat_id}")

async def main():
    token = os.getenv("BOT_TOKEN","7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o")
    app = ApplicationBuilder().token(token).build()

    # Handler para mensajes normales (grupos o privados)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    # Handler para mensajes en canales
    app.add_handler(ChannelPostHandler(handle_channel_post))

    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(main())

