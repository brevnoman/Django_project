import datetime
import time
from telegram_bot.models import Meetings, Session, User
from sqlalchemy.sql.expression import func

def say_me_when(bot, update):
    session = Session()
    while True:
        meetings = session.query(Meetings).filter(Meetings.is_accepted==True).all()
        for meeting in meetings:
            if str(datetime.datetime.now() + datetime.timedelta(days=1))[:13] == str(datetime.datetime.combine(meeting.date, meeting.time_start))[:13]:
                text = f"Завтра у вас встреча с {session.query(User.first_name, User.last_name).filter(User.id==meeting.user_id).first()}  c {meeting.time_start} до {meeting.time_end}\n"
                update.bot.send_message(chat_id=bot.effective_chat.id, text=text)
        time.sleep(3600)



session = Session()

# date_max = session.query(Meetings, func.max()).group_by(Meetings.date).first()
res = session.query(Meetings, func.max(func.coalesce(Meetings.date, datetime.date.today()-datetime.timedelta(days=10)))
).group_by(Meetings.id).all()
# print(date_max)
print(date)
