import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    active_passcards = []
    for passcard in passcards.values():
        if passcard['is_active']:
            active_passcards.append(passcard)
    print('Всего пропусков', passcards.count())
    print('Активных пропусков', len(active_passcards))
