from django.conf import settings
from django.http import JsonResponse


async def healthcheck(request):
    return JsonResponse(
        {
            "release_version": settings.RELEASE_VERSION,
            "hash": settings.GIT_HASH,
        }
    )
