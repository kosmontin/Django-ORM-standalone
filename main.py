import datetime
import os

import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Visit
from datacenter.models import Passcard

if __name__ == '__main__':
    visits = []
    for passcard in Passcard.objects.all()[0]:
        visits.append(Visit.objects.filter(passcard=passcard))
    print(*visits[0], sep='\n')
    # visits = Visit.objects.filter()
    # for visit in visits:
    #     print(visit.passcard.owner_name)
    #     leaved_at = timezone.localtime()
    #     entered_at = timezone.localtime(visit.entered_at)
    #     time_delta = (leaved_at - entered_at)
    #     print(f'Зашёл в хранилище, время по Москве:\n'
    #           f'{entered_at}\n'
    #           f'Находится в хранилище:\n'
    #           f'{time_delta}\n')
