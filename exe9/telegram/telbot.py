from telegram.ext import ApplicationBuilder, CommandHandler

app = ApplicationBuilder().token("1903908474:AAGU-PLODiwJ4fJGNE73SRDH7BvN51n6lds").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()