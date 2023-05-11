from django.http import JsonResponse
from django.views import View
from ..models.country_timezone import Timezone
import json


class CreateTimezoneView(View):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        country = payload.get('country')
        timezone = payload.get('timezone')
        timezone = Timezone(country=country, timezone=timezone)
        timezone.save()
        data = {
            'id': timezone.id,
            'country': timezone.country,
            'timezone': timezone.timezone
        }
        print(data)
        return JsonResponse({'timezone': data})


class ListTimezoneView(View):
    def get(self, request, *args, **kwargs):
        timezones = Timezone.objects.all()
        data = []
        for timezone in timezones:
            data.append({
                'id': timezone.id,
                'country': timezone.country,
                'timezone': timezone.timezone
            })
        return JsonResponse(data, safe=False)
