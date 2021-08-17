import datetime
import time
from background_task import background
from main_app.models import Conclusion, Meeting


def calendar_util(year, month):
    current_month_list = []
    current_year = int(year)
    current_month = int(month)
    current_month_text = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    first_day_of_current_month = datetime.datetime(year=current_year, month=current_month, day=1).weekday()
    previous_month = (datetime.datetime(year=current_year, month=current_month, day=1)-datetime.timedelta(days=15)).month
    previous_year = (datetime.datetime(year=current_year, month=current_month, day=1)-datetime.timedelta(days=15)).year
    next_month = (datetime.datetime(year=current_year, month=current_month, day=27)+datetime.timedelta(days=15)).month
    next_year = (datetime.datetime(year=current_year, month=current_month, day=27)+datetime.timedelta(days=15)).year
    month_for_now = datetime.datetime.today().month
    year_for_now = datetime.datetime.today().year
    today = datetime.date.today()
    first_week = True
    day = 1
    meetings = show_all_meetings()
    current_week = []
    try:
        for _ in range(6):
            current_week = []
            for i in range(7):
                if first_week and i < first_day_of_current_month:
                    current_week += "_"
                else:
                    meet_is_true = False
                    needed_meet = ""
                    for meet in meetings:
                        if datetime.datetime(year=current_year,
                                             month=current_month,
                                             day=day).month == meet.date.month and datetime.datetime(year=current_year,
                                                                                                     month=current_month,
                                                                                                     day=day).day == meet.date.day:
                            meet_is_true = True
                            needed_meet = meet
                    if meet_is_true:
                        if not needed_meet.is_done:
                            html = f'<a href="/user_page/meetings_of_date/{needed_meet.date}" class="btn btn-primary btn-sm"><h6>{str(needed_meet.date)[8:10]}</h6</a>'
                            current_week.append(html)
                        else:
                            html = f'<a href="/user_page/meetings_of_date/{needed_meet.date}" class="btn btn-info btn-sm"><h6>{str(needed_meet.date)[8:10]}</h6</a>'
                            current_week.append(html)
                    else:
                        if day < 10:
                            current_week.append(f'<a class="btn btn-light btn-sm"><h6>0{day}</h6</a>')
                        else:
                            current_week.append(f'<a class="btn btn-light btn-sm"><h6>{day}</h6</a>')
                    day += 1
            first_week = False
            current_month_list.append(current_week)
    except ValueError:
        for i in range(6 - datetime.datetime(year=current_year, month=current_month, day=day-1).weekday()):
            current_week += "_"
        current_month_list.append(current_week)
    return {
        "cal": current_month_list,
        'year': year_for_now,
        "month": month_for_now,
        "previous_month": previous_month,
        "next_month": next_month,
        "previous_year":previous_year,
        'next_year': next_year,
        "current_month_text": current_month_text[current_month-1],
        "now_year": current_year,
        "now_month": current_month,
        "today": today
    }


def show_undone_meetings():
    meetings = Meeting.objects.filter(is_accepted=True, is_done=False).order_by("date").all()
    return meetings

def show_all_meetings():
    meetings = Meeting.objects.filter(is_accepted=True).order_by("date").all()
    return meetings

def get_user_meetings(request):
    user_meetings = Meeting.objects.filter(user=request.user, is_accepted=True).order_by("date").all()
    return user_meetings


def get_user_conclusions(meeting):
    user_conclusions = Conclusion.objects.filter(meeting=meeting).all()
    return user_conclusions


