from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters, ContextTypes

# Estados del formulario
NUMERO, AUTORIZA, RESPONSABLE, FECHA, MONTO, PTOT, CONCEPTO, LOCALIDAD, SER = range(9)

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

    # Crear mensaje final
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

    # Envía al grupo y al usuario
    chat_id_grupo = -1001234567890  # <<--- aquí pones el ID de tu grupo
    await update.message.reply_text("¡Formulario completado! Publicando...")
    await context.bot.send_message(chat_id=chat_id_grupo, text=mensaje)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Formulario cancelado.')
    return ConversationHandler.END

app = ApplicationBuilder().token('7714496610:AAG91ImaiK5EKH5Dcn1kjTn6T3w-GRD0Y4o').build()

# Definir el flujo
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        NUMERO: [MessageHandler(filters.TEXT, numero)],
        AUTORIZA: [MessageHandler(filters.TEXT, autoriza)],
        RESPONSABLE: [MessageHandler(filters.TEXT, responsable)],
        FECHA: [MessageHandler(filters.TEXT, fecha)],
        MONTO: [MessageHandler(filters.TEXT, monto)],
        PTOT: [MessageHandler(filters.TEXT, ptot)],
        CONCEPTO: [MessageHandler(filters.TEXT, concepto)],
        LOCALIDAD: [MessageHandler(filters.TEXT, localidad)],
        SER: [MessageHandler(filters.TEXT, ser)],
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

app.add_handler(conv_handler)

app.run_polling()
