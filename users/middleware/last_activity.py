from django.contrib.auth import get_user_model


class BaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class UpdateUserLastActivityMiddleware(BaseMiddleware):
    @staticmethod
    def process_view(request, *_):
        if request.user.is_authenticated:
            get_user_model().objects.get(pk=request.user.pk).save()
        return None
