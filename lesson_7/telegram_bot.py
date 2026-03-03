import os
import ptbot
from dotenv import load_dotenv
import random
from pytimeparse import parse


def announce(chat_id, question, bot):
    total_secs = parse(question)
    secs_left = total_secs
    text_start = "Starting timer..."
    message_id = bot.send_message(chat_id, text_start)
    bot.create_timer(secs_left, notify_ending, chat_id=chat_id, bot=bot)
    bot.create_countdown(secs_left, notify_progress, chat_id=chat_id, message_id=message_id, total=total_secs, bot=bot)


def notify_progress(secs_left, bot, chat_id, message_id, total):
    message = f"{secs_left} sec's left!\n {render_progressbar(total, secs_left)}"
    bot.update_message(chat_id, message_id, message)


def notify_ending(chat_id, bot):
    text_end = "Time's up!"
    bot.send_message(chat_id, text_end)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    load_dotenv()
    tg_token = os.getenv("tg_token")
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(announce, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
