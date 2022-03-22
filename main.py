import datetime
import os

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit

if __name__ == '__main__':
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        print(visit.passcard.owner_name)
        leaved_at = timezone.localtime()
        entered_at = timezone.localtime(visit.entered_at)
        time_delta = (leaved_at - entered_at)
        print(f'Зашёл в хранилище, время по Москве:\n'
              f'{entered_at}\n'
              f'Находится в хранилище:\n'
              f'{time_delta}\n')
