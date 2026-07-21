from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from database import *

TOKEN = ""TOKEN = "8307409670:AAGDvUGaeBnvbsiZDDBXrxfuM4DLXFEIfyw"

create_tables()

app = ApplicationBuilder().token(TOKEN).build()
