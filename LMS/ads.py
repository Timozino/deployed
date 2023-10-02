from django.http import HttpResponse
from django.views import View

class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    line  =  "google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0"
    def get(self, request, *args, **kwargs):
        return HttpResponse("google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0")