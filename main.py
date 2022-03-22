import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':
    visits = Visit.objects.filter(leaved_at__isnull=True)
    print(*visits, sep='\n')
