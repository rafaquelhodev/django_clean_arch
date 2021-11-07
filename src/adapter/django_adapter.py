from rest_framework.response import Response


class DjangoAdapter:
    @staticmethod
    def create(fn, request, serializer, **kwargs):
        res, status = fn(request.data, serializer, **kwargs)
        return Response(res, status)
