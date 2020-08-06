from django.http import HttpResponse
from django.views import View


# class-based view
class WorkerListView(View):
    def get(self, request):
        return HttpResponse()