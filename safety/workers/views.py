from django.http import HttpResponse
from django.views import View

from .models import Worker


# class-based view
class WorkerListView(View):
    def get(self, request):
        workers = Worker.objects.all()
        print(workers)
        html = ''
        for worker in workers:
            html += f'<li>{worker.first_name}</li>'

        return HttpResponse(html)