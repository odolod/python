from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token("1903908474:AAGU-PLODiwJ4fJGNE73SRDH7BvN51n6lds").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("power", power_command))



app.run_polling()