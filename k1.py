
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# استخدام الـ BOT_TOKEN الخاص بك
BOT_TOKEN = '7609502903:AAFsuRnn2RJl10e2uz5MmIhJZmmL8iV8LnI'

# روابط الأزرار المخصصة
custom_button_url = "https://www.dzrt.com/ar-sa/category/nicotine-pouches"
custom_button_text = "قائمة المنتجات 📦"
login_button_url = "https://www.dzrt.com/ar-sa/login/mobile-number"
login_button_text = "تسجيل الدخول 🔐"

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # تحقق من وجود المنشور في القناة
        print("Received a channel post.")
        if update.channel_post:
            print(f"Post from chat: {update.channel_post.chat_id}, Chat type: {update.channel_post.chat.type}")

            # التحقق مما إذا كانت الرسالة أو الوصف تحتوي على الملصق "💎"
            message_text = update.channel_post.text or update.channel_post.caption or ""
            if "💎" in message_text:
                print("Message or caption contains the green circle emoji.")

                # إنشاء الأزرار
                keyboard = [
                    [InlineKeyboardButton(custom_button_text, url=custom_button_url)],
                    [InlineKeyboardButton(login_button_text, url=login_button_url)]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                # تعديل المنشور الأصلي لإضافة الأزرار
                await context.bot.edit_message_reply_markup(
                    chat_id=update.channel_post.chat_id,
                    message_id=update.channel_post.message_id,
                    reply_markup=reply_markup
                )
                print(f'Edited message in chat {update.effective_chat.id} to add buttons.')
            else:
                print("Message or caption does not contain the green circle emoji.")
        else:
            print("No channel post found.")
    except Exception as e:
        print(f'Error: {e}')

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # إضافة معالج المنشورات في القناة
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_channel_post))

    # بدء تشغيل البوت
    print('Bot is running...')
    application.run_polling()

if __name__ == '__main__':
    main()
