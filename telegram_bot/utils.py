import logging
import datetime


def get_logger():
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    return logger


meeting_time = datetime.datetime.utcnow()
print(type(meeting_time))
print(str(meeting_time)[:10])
print(str(datetime.datetime.today())[:10])
print(str(meeting_time)[:10]==str(datetime.datetime.today())[10])