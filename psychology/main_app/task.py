import datetime
from background_task import background
from main_app.utils import show_all_meetings


@background(schedule=10)
def is_done_meeting():
    meetings = show_all_meetings()
    for meeting in meetings:
        if datetime.datetime.combine(meeting.date, meeting.time_end) <= datetime.datetime.now():
            meeting.is_done = True
            meeting.save()
        else:
            if meeting.is_done:
                meeting.is_done = False
                meeting.save()
