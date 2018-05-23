import pytz
from your_appplication.settings import TIME_ZONE
from django.utils.timezone import now

class DateTime():
    def __init__(self, date_time=None, format=None, time_zone=None):
        self.date_time = now() if date_time is None else date_time
        self.format = '%Y-%m-%d %H:%M:%S' if format is None else format
        self.time_zone = pytz.timezone(TIME_ZONE) if time_zone is None else pytz.timezone(time_zone)

    def __str__(self):
        return self.date_time.astimezone(self.time_zone).strftime(self.format)

    def timezone_month(self):
        return self.date_time.astimezone(self.time_zone).month

    def timezone_month_zero(self):
        return '%02d' % (self.date_time.astimezone(self.time_zone).month)

    def timezone_day(self):
        return self.date_time.astimezone(self.time_zone).day

    def timezone_day_zero(self):
        return '%02d' % (self.date_time.astimezone(self.time_zone).day)

    def timezone_year(self):
        return self.date_time.astimezone(self.time_zone).year