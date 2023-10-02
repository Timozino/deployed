class AdBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.content = response.content.replace(
            b'</body>',
            b'<script src="{% static "assets/js/adblocker.js" %}"></script></body>',
        )
        return response