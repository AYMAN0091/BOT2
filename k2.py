from telethon import TelegramClient, events
import re

# إعدادات البوت (استخدام معلوماتك الخاصة)
api_id = '29603702'
api_hash = '448c9888446f6bdd2484ee840fc04650'
phone = '+966558659183'  # رقم هاتف حساب تيليجرام الخاص بك
source_channel_id = -1002266160751  # ID القناة المصدر
target_channel_id = -1002258696230  # ID القناة الهدف

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel_id))
async def forward_specific_message(event):
    message_text = event.message.message or event.message.caption or ""

    # التحقق مما إذا كانت الرسالة تحتوي على الأنماط المختلفة
    match_available_1 = re.search(r"🟢 المنتج متوفر : (.+)", message_text)
    match_unavailable_1 = re.search(r"🔴 المنتج نفذ من المخزون : (.+)", message_text)
    match_available_2 = re.search(r"المنتج ↞【(.+)】✅️", message_text)
    match_unavailable_1 = re.search(r"🧿 المنتج : 【(.+)】", message_text)
    
    if match_available_1:
        product_name = match_available_1.group(1).strip()  # استخراج اسم المنتج
        new_message = f"{product_name} : متوفر الآن 💎"
        
        # إذا كانت الرسالة تحتوي على صورة، أرسل الصورة مع النص الجديد
        if event.message.photo:
            await client.send_file(
                target_channel_id,
                file=event.message.media,
                caption=new_message
            )
        else:
            # إرسال النص فقط إذا لم تكن هناك صورة
            await client.send_message(target_channel_id, new_message)
        
        print(f'Message with "{product_name}" (available) forwarded with new content.')
    
    elif match_unavailable_1:
        product_name = match_unavailable_1.group(1).strip()  # استخراج اسم المنتج
        new_message = f"{product_name} : نفذ❌"
        
        # إذا كانت الرسالة تحتوي على صورة، أرسل الصورة مع النص الجديد
        if event.message.photo:
            await client.send_file(
                target_channel_id,
                file=event.message.media,
                caption=new_message
            )
        else:
            # إرسال النص فقط إذا لم تكن هناك صورة
            await client.send_message(target_channel_id, new_message)
        
        print(f'Message with "{product_name}" (unavailable) forwarded with new content.')
    
    elif match_available_2:
        product_name = match_available_2.group(1).strip()  # استخراج اسم المنتج
        new_message = f"{product_name} : متوفر الآن 💎"
        
        if event.message.photo:
            await client.send_file(
                target_channel_id,
                file=event.message.media,
                caption=new_message
            )
        else:
            await client.send_message(target_channel_id, new_message)
        
        print(f'Message with "{product_name}" (available) forwarded with new content (pattern 2).')
    
    elif match_available_3:
        product_name = match_available_3.group(1).strip()  # استخراج اسم المنتج
        new_message = f"{product_name} : متوفر الآن 💎"
        
        if event.message.photo:
            await client.send_file(
                target_channel_id,
                file=event.message.media,
                caption=new_message
            )
        else:
            await client.send_message(target_channel_id, new_message)
        
        print(f'Message with "{product_name}" (available) forwarded with new content (pattern 3).')
    
    else:
        print("Message does not match any pattern. No action taken.")

print("Bot is running...")
client.start(phone)
client.run_until_disconnected()
