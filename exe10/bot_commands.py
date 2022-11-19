from telegram import Update
from telegram.ext import ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Команды:\n/hello\n/sum\n/mult\n/power\n/start')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def power_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    items = update.message.text.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ^ {y} = {x**y}')