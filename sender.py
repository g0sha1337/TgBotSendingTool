import asyncio
import argparse
from loguru import logger
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

import config

sent = 0 
failed = 0

async def send_notifications(text_file, image_file, gif_file, inline_file, database_file):
    
    bot = Bot(token=config.TelegramBotToken)
    global sended
    global failed

    try:

        if database_file:
            with open(database_file, 'r') as file:
                user_ids = [line.strip() for line in file.readlines() if line.strip().isdigit()]
        else: #ids.txt for default
            with open('ids.txt', 'r') as file:
                user_ids = [line.strip() for line in file.readlines() if line.strip().isdigit()]

        if text_file:
            with open(text_file, 'r', encoding='utf-8') as f:
                message = f.read()
        else:
            logger.error(f"Error with reading {text_file}!")

        inline_keyboard = None
        if inline_file:
            with open(inline_file, 'r', encoding='utf-8') as f: # open inline button file in format ExampleName, ExampleLink
                button_data = f.readlines()
                buttons = []
                for line in button_data:
                    text, url = line.strip().split(',')
                    buttons.append([InlineKeyboardButton(text=text, url=url.replace(' ',''))])
                inline_keyboard = InlineKeyboardMarkup(buttons)

        for user_id in user_ids:
            try:
                if inline_keyboard:
                    if image_file:
                        with open(image_file, 'rb') as img:
                            await bot.send_photo(chat_id=user_id, photo=img, caption=message, parse_mode='Markdown', reply_markup=inline_keyboard)
                    elif gif_file:
                        with open(gif_file, 'rb') as gif:
                            await bot.send_animation(chat_id=user_id, animation=gif, caption=message, parse_mode='Markdown', reply_markup=inline_keyboard)
                    else :
                        await bot.send_message(chat_id=user_id, text=message,parse_mode='Markdown',  reply_markup=inline_keyboard)
                else: 
                    if image_file:
                        with open(image_file, 'rb') as img:
                            await bot.send_photo(chat_id=user_id, photo=img, caption=message, parse_mode='Markdown',)
                    elif gif_file:
                        with open(gif_file, 'rb') as gif:
                            await bot.send_animation(chat_id=user_id, animation=gif, caption=message, parse_mode='Markdown',)
                    else :
                        await bot.send_message(chat_id=user_id, text=message, parse_mode='Markdown',)

                logger.info(f"Message sent to {user_id}")
                sent += 1
            except Exception as e:
                logger.error(f"Error with sending message to {user_id}: {e}")
                failed +=1

        logger.success(f"All messages were sent! Total successfully sent: {sent}, failed: {failed}")
    except Exception as e:
        logger.error(f"Some error accured: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send notifications via Telegram bot.')
    parser.add_argument('--text', type=str, help='Path to the text file')
    parser.add_argument('--image', type=str, help='Path to the image file')
    parser.add_argument('--gif', type=str, help='Path to the GIF file')
    parser.add_argument('--inline', type=str, help='Path to the inline button link info file')
    parser.add_argument('--database', type=str, help='Path to the id database file')

    args = parser.parse_args()

    asyncio.run(send_notifications(args.text, args.image, args.gif, args.inline, args.database))