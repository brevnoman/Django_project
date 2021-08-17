import datetime
import time
from telegram_bot.models import Meeting, Session, User


def say_me_when(bot, update):
    session = Session()
    repeat_time = 3600
    while True:
        meetings = session.query(Meeting).filter(Meeting.is_accepted == True).all()
        print('hi')
        for meeting in meetings:
            if str(datetime.datetime.now() + datetime.timedelta(days=1))[:13] == str(
                    datetime.datetime.combine(meeting.date, meeting.time_start))[:13]:
                text = f"Завтра у вас встреча с {session.query(User.first_name, User.last_name).filter(User.id == meeting.user_id).first()}  c {meeting.time_start} до {meeting.time_end}\n"
                update.bot.send_message(chat_id=bot.effective_chat.id, text=text)
            elif str(datetime.datetime.now() + datetime.timedelta(hours=1))[:13] == str(
                    datetime.datetime.combine(meeting.date, meeting.time_start))[:13]:
                text = f"Через час у вас встреча с {session.query(User.first_name, User.last_name).filter(User.id == meeting.user_id).first()}  c {meeting.time_start} до {meeting.time_end}\n"
                update.bot.send_message(chat_id=bot.effective_chat.id, text=text)
        time.sleep(repeat_time)
