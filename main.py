import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    passcards = Passcard.objects.all().values()
    print(f'owner_name:\t{passcards[0]["owner_name"]}\n'
          f'passcode:\t{passcards[0]["passcode"]}\n'
          f'created_at:\t{passcards[0]["created_at"]}\n'
          f'is_active:\t{passcards[0]["is_active"]}')
