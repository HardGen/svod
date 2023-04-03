from django_cron import CronJobBase, Schedule
from .models import *
import datetime

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS  = 2
    schedule = Schedule( run_every_mins=RUN_EVERY_MINS )
    code = 'app.my_cron_job'

    def do(self):
        with open('cron.txt', 'w') as f:
            f.write(datetime.datetime.today().isoformat())


