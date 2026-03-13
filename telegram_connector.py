import telebot

# Replace this with your actual Telegram Bot Token
# NOTE: Before pushing to GitHub, we will hide this token in a secure environment variable.
TELEGRAM_TOKEN = TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # We will connect this to a .env file later for security

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Command handler for /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Hello! I am your OmniAgents Core Assistant. 🚀\n\n"
        "I am currently active and listening. My AI modules are being integrated, so stay tuned!"
    )
    bot.reply_to(message, welcome_text)

# Message handler for all other text messages
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_text = message.text
    response_text = f"You said: '{user_text}'.\n(My AI core is currently offline. I will be fully functional soon!)"
    bot.reply_to(message, response_text)

if __name__ == "__main__":
    print("🚀 Telegram Bot is running in the background...")
    # This keeps the bot running continuously
    bot.infinity_polling()