from django.http import HttpResponse
from django.views import View

import requests


class Covid19ReportView(View):
    def get(self, request):
        r = requests.get('https://covid19.th-stat.com/api/open/today')
        data = r.json()
        new_confirmed = data['NewConfirmed']

        return HttpResponse(f'NewConfirmed: {new_confirmed}')
