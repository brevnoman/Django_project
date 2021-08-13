import datetime

from django.shortcuts import render, redirect
from main_app.forms import NewUserForm, MeetingCreateForm, NewUserChangeForm, User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from main_app.models import Meeting, Conclusion


def date_meetings(request, meetings_date):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    meetings = Meeting.objects.filter(is_accepted=True, is_done=False, date=meetings_date).order_by("time_start").all()
    return render(request, "user_page_meetings.html", context={"meetings": meetings, 'year': current_year, "month": current_month})

#delete it
def calendar(request, year= datetime.datetime.today().year, month=datetime.datetime.today().month):
    current_month_list = []
    current_year = int(year)
    current_month = int(month)
    current_month_text = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    first_day_of_current_month = datetime.datetime(year=current_year, month=current_month, day=1).weekday()
    previous_month = (datetime.datetime(year=current_year, month=current_month, day=1)-datetime.timedelta(days=15)).month
    previous_year = (datetime.datetime(year=current_year, month=current_month, day=1)-datetime.timedelta(days=15)).year
    print(previous_month)
    next_month = (datetime.datetime(year=current_year, month=current_month, day=27)+datetime.timedelta(days=15)).month
    next_year = (datetime.datetime(year=current_year, month=current_month, day=27)+datetime.timedelta(days=15)).year
    print(next_month)
    first_week = True
    day = 1
    meetings = show_undone_meetings()
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
                        if datetime.datetime(year=current_year, month=current_month, day=day).month == meet.date.month and datetime.datetime(year=current_year, month=current_month, day=day).day == meet.date.day:
                            print(datetime.datetime(year=current_year, month=current_month, day=day).day)
                            print(meet.date.day)
                            print("kukusiki")
                            meet_is_true = True
                            needed_meet = meet
                    if meet_is_true:
                        html = f'<a href="/user_page/meetings_of_date/{needed_meet.date}">{str(needed_meet.date)[8:10]}</a>'
                        current_week.append(html)
                        meet_is_true = False
                    else:
                        if day < 10:
                            current_week.append(f"0{day}")
                        else:
                            current_week.append(day)
                    day += 1
            first_week = False
            current_month_list.append(current_week)
    except ValueError:
        for i in range(6 - datetime.datetime(year=current_year, month=current_month, day=day-1).weekday()):
            current_week += "_"
        current_month_list.append(current_week)
    html_thing = '<a href="/user_page/meetings/"><h4>Открыть</h4></a>'
    just_number = "5"
    print(current_month_list)
    return render(request, "Backup.html", context={"cal": current_month_list,
                                                   "html_code": html_thing,
                                                   'num': just_number,
                                                   'year': current_year,
                                                   "month": current_month,
                                                   "previous_month": previous_month,
                                                   "next_month": next_month,
                                                   "previous_year":previous_year,
                                                   'next_year': next_year,
                                                   "current_month_text": current_month_text[current_month-1]})


def user_page(request):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    print(current_year, current_month)
    return render(request, "user_page.html", context={'year': current_year, "month": current_month})

def user_page_personal_inform(request):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    return render(request, "user_personal_inform.html", context={'year': current_year, "month": current_month})

def user_page_meetings(request):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    if request.user.is_superuser:
        user_meetings = show_undone_meetings()
    else:
        user_meetings = get_user_meetings(request)
    return render(request, "user_page_meetings.html", context={"meetings": user_meetings,'year': current_year, "month": current_month})

def meeting_conclusion(request, meeting):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    user_conclusions = get_user_conclusions(meeting)
    if request.user.is_superuser:
        meeting = Meeting.objects.get(id=meeting)
    else:
        meeting = Meeting.objects.get(id=meeting, user_id=request.user.id)
    return render(request, "user_page_conclusions.html", context={"conclusions": user_conclusions, "meeting": meeting, 'year': current_year, "month": current_month})

def render_main_page(request):
    return render(request, "main_page.html")

def loguot_user(request):
    logout(request)
    return render(request, "main_page.html")


def create_meeting(request):
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    if request.method == "POST":
        form = MeetingCreateForm(request.POST)
        if form.is_valid():

            form.user = request.user
            print(form.user)
            meeting = form.save(commit=False)
            meeting.user = request.user
            print(meeting.user)
            meeting.save()
            messages.success(request, "Заявка откправлена")
            return redirect("/user_page")
        messages.error(request, "Не верно заполнена форма.")
    form = MeetingCreateForm()
    return render(request=request, template_name="meeting_create.html", context={"meeting_form": form, 'year': current_year, "month": current_month})


def register_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.first_name = request.POST["first_name"]
            print(form.first_name)
            form.last_name = request.POST["last_name"]
            print(form.last_name)
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})



def get_user_meetings(request):
    user_meetings = Meeting.objects.filter(user=request.user, is_accepted=True).order_by("date").all()
    return user_meetings

def get_user_conclusions(meeting):
    user_conclusions = Conclusion.objects.filter(meeting=meeting).all()
    # print(user_conclusions)
    return user_conclusions

def user_page_editing(request):
    if request.method == "POST":
        form = NewUserChangeForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            form = form.save(commit=False)
            user.username = form.username
            user.first_name = form.first_name
            user.last_name = form.last_name
            user.email = form.email
            user.save()
            messages.success(request, "Аккаунт изменён")
            return redirect("/user_page")
        messages.error(request, "Не верно указаны данные")
    form = NewUserChangeForm()
    form.base_fields["first_name"].initial = request.user.first_name
    form.base_fields["last_name"].initial = request.user.last_name
    form.base_fields["email"].initial = request.user.email
    form.base_fields["username"].initial = request.user.username
    current_year = datetime.datetime.today().year
    current_month = datetime.datetime.today().month
    return render(request=request, template_name="user_page_edit.html", context={"meeting_form": form, 'year': current_year, "month": current_month})



def show_undone_meetings():
    meetings = Meeting.objects.filter(is_accepted=True, is_done=False).order_by("date").all()
    return meetings