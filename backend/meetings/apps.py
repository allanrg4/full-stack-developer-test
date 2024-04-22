import sys
import json
from datetime import datetime

from django.conf import settings
from django.apps import AppConfig
from django.utils import timezone


class MeetingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meetings'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from meetings.models import Session

        date_format = '%d/%m/%Y %H:%M'

        filename = settings.BASE_DIR / 'fixtures' / 'sessions.json'
        with open(filename, 'r') as file:
            sessions: dict = json.load(file).get('sessions')

            for name, schedules in sessions.items():
                for schedule in schedules:
                    start_datetime = schedule.get('start_datetime')
                    start_datetime = datetime.strptime(start_datetime, date_format)
                    start_datetime = timezone.make_aware(start_datetime)

                    end_datetime = schedule.get('end_datetime')
                    end_datetime = datetime.strptime(end_datetime, date_format)
                    end_datetime = timezone.make_aware(end_datetime)

                    availability = schedule.get('availability')

                    Session.objects.get_or_create(
                        name=name,
                        start_datetime=start_datetime,
                        end_datetime=end_datetime,
                        availability=availability
                    )
