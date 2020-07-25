import datetime

from django.shortcuts import render

# Create your views here.
from django.views import View


class BookView(View):

    def get(self, request):
        content = {
            "persons": {
                "name": ["张贺凡", "熊淑萍"],
                "age": [18, 40],
                "time": datetime.datetime.now()
            }
        }
        hello = "me"
        return render(request, "index.html", context=content)

    def post(self, request):
        return self.get(request)
