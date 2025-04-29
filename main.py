from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"El ID de este canal/grupo es: {chat_id}")

async def main():
    token = os.getenv("BOT_TOKEN","7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o")
    app = ApplicationBuilder().token(token).build()
    
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

