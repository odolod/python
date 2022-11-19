from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token("1903908474:AAGU-PLODiwJ4fJGNE73SRDH7BvN51n6lds").build()

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("generate", generate_command))
app.add_handler(CommandHandler("find", find_command))
app.add_handler(CommandHandler("findp", findp_command))
app.add_handler(CommandHandler("finds", finds_command))
app.add_handler(CommandHandler("add", add_command))
app.add_handler(CommandHandler("delete", delete_command))
app.add_handler(CommandHandler("update", update_command))

app.run_polling()