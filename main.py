import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes
import nest_asyncio

# Estados del formulario
NUMERO, AUTORIZA, RESPONSABLE, FECHA, MONTO, PTOT, CONCEPTO, LOCALIDAD, SER = range(9)

# Leer ID del canal desde variable de entorno
CHAT_ID_GRUPO = int(os.getenv('CHAT_ID_GRUPO', '-1002595768515'))  # Cambia aquí si quieres

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bienvenido. ¿Número de depósito?')
    return NUMERO

async def numero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['numero'] = update.message.text
    await update.message.reply_text('¿Quién autoriza?')
    return AUTORIZA

async def autoriza(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['autoriza'] = update.message.text
    await update.message.reply_text('¿Responsable?')
    return RESPONSABLE

async def responsable(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['responsable'] = update.message.text
    await update.message.reply_text('¿Fecha de ejecución?')
    return FECHA

async def fecha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['fecha'] = update.message.text
    await update.message.reply_text('¿Monto (Soles)?')
    return MONTO

async def monto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['monto'] = update.message.text
    await update.message.reply_text('¿PT y/o OT?')
    return PTOT

async def ptot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['ptot'] = update.message.text
    await update.message.reply_text('¿Concepto?')
    return CONCEPTO

async def concepto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['concepto'] = update.message.text
    await update.message.reply_text('¿Localidad?')
    return LOCALIDAD

async def localidad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['localidad'] = update.message.text
    await update.message.reply_text('¿SER?')
    return SER

async def ser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['ser'] = update.message.text

    mensaje = f"""
Saludos, Fátima favor según lo siguiente realizar el depósito.

Depósito
N°            : {context.user_data['numero']}
Autoriza      : {context.user_data['autoriza']}
Responsable   : {context.user_data['responsable']}
Fecha Ejecución: {context.user_data['fecha']}
Monto(Soles)  : {context.user_data['monto']}
PT y/o OT     : {context.user_data['ptot']}
Concepto      : {context.user_data['concepto']}
Localidad     : {context.user_data['localidad']}
SER           : {context.user_data['ser']}

Asimismo remitir el depósito (yape, plin o transferencia bancaria), en caso de otra modalidad detallar cómo se realizó el depósito.
"""

    await update.message.reply_text("¡Formulario completado! Publicando...")
    await context.bot.send_message(chat_id=CHAT_ID_GRUPO, text=mensaje)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Formulario cancelado.')
    return ConversationHandler.END

# Inicializar aplicación
async def main():
    token = os.getenv('BOT_TOKEN','7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o')
    app = ApplicationBuilder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NUMERO: [MessageHandler(filters.TEXT & (~filters.COMMAND), numero)],
            AUTORIZA: [MessageHandler(filters.TEXT & (~filters.COMMAND), autoriza)],
            RESPONSABLE: [MessageHandler(filters.TEXT & (~filters.COMMAND), responsable)],
            FECHA: [MessageHandler(filters.TEXT & (~filters.COMMAND), fecha)],
            MONTO: [MessageHandler(filters.TEXT & (~filters.COMMAND), monto)],
            PTOT: [MessageHandler(filters.TEXT & (~filters.COMMAND), ptot)],
            CONCEPTO: [MessageHandler(filters.TEXT & (~filters.COMMAND), concepto)],
            LOCALIDAD: [MessageHandler(filters.TEXT & (~filters.COMMAND), localidad)],
            SER: [MessageHandler(filters.TEXT & (~filters.COMMAND), ser)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    app.add_handler(conv_handler)

    await app.run_polling()

# Correr el bot
if __name__ == "__main__":
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())


