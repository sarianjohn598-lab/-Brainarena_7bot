import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging to see errors in Railway logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Retrieve token from Railway Environment Variables
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the BrainArena welcome message when /start is issued."""
    welcome_text = (
        "Welcome to BrainArena! 🎯\n\n"
        "We're here to make learning fun through exciting quizzes, logic puzzles, and daily brain challenges. "
        "Test your knowledge, sharpen your mind, and compete for the top spot!\n\n"
        "Challenge your mind with daily quizzes, brain teasers, and fun puzzles. "
        "Earn points and climb the leaderboard!"
    )
    await update.message.reply_text(welcome_text)

def main() -> None:
    """Start the bot."""
    # Build the application
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot (Long Polling)
    # drop_pending_updates=True prevents processing old messages after a restart
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
