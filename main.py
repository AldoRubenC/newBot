import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import nest_asyncio

# Función para manejar mensajes normales y posts de canales
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        # Mensaje en privado o grupo
        chat_id = update.effective_chat.id
        await update.message.reply_text(f"El ID de este chat es: {chat_id}")
    elif update.channel_post:
        # Post en un canal
        chat_id = update.effective_chat.id
        await update.channel_post.reply_text(f"El ID de este canal es: {chat_id}")

async def main():
    token = os.getenv("BOT_TOKEN","7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o")
    app = ApplicationBuilder().token(token).build()

    # Captura tanto mensajes como posts de canales
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()
        asyncio.get_event_loop().run_until_complete(main())

