from django_cron import CronJobBase, Schedule
from .models import *

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS=1
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'app.my_cron_job'

    def do(self):
        Food_svod.objects.create(idotd_id=7082)