۸from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from database import create_tables

TOKEN="8307409670:AAGDvUGaeBnvbsiZDDBXrxfuM4DLXFEIfyw"

create_tables()

keyboard = ReplyKeyboardMarkup(
    [
        ["➕ ثبت ذکر"],
        ["📊 آمار"],
        ["ℹ️ راهنما"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 🌸\n\nبه ربات ثبت ذکر خوش آمدید.\n\nبرای شروع یکی از گزینه‌های زیر را انتخاب کنید.",
        reply_markup=keyboard
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
