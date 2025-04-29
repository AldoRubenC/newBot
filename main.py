from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def get_group_id(update: Update, context):
    chat_id = update.message.chat.id
    await update.message.reply_text(f"El ID de este grupo es: {chat_id}")

async def main():
    token = os.getenv("7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o")
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler("getgroupid", get_group_id))
    
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

