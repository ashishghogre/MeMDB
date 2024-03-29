from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'games': reverse('games:game-list', request=request, format=format),
        'team': reverse('team:team', request=request, format=format),
    })