# File: bot.py
# The EASIEST Telegram bot in 2025-2026 style

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# ─── CHANGE THIS ────────────────────────────────
TOKEN = "YOUR_BOT_TOKEN_HERE"   # ← Put your token here
# ─────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Yo bro! I'm alive 🔥\n"
        "Just send me anything and I'll echo it back 😏\n\n"
        "Commands:\n/start - wake me up\n/help - this message"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I'm a very simple bot bro 😭\n"
        "• Send any message → I repeat it\n"
        "• /start → say hi\n"
        "• Just vibe, that's all for now!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Reply with the same message the user sent
    await update.message.reply_text(update.message.text)


async def main():
    print("Starting bot... 🚀")

    # Build the application
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Echo ALL normal text messages (not commands)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot (polling = easiest way)
    await app.initialize()
    await app.start()
    await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)

    print("Bot is running! Talk to him on Telegram 😎")
    
    # Keep running until you press Ctrl+C
    await app.updater.idle()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
