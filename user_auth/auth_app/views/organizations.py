from django.views import View
from django.http import JsonResponse
from ..models.organizations import Organizations
import json


class CreateOrganizationView(View):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        name = payload.get('name')
        description = payload.get('description')
        address = payload.get('address')
        organization = Organizations(name=name, description=description, address=address)
        organization.save()
        data = {
            'id': organization.id,
            'name': organization.name,
            'description': organization.description,
            'address': organization.address
        }
        return data


class ListOrganizationsView(View):
    def get(self, request, *args, **kwargs):
        organizations = Organizations.objects.all()
        data = []
        for organization in organizations:
            data.append({
                'id': organization.id,
                'name': organization.name,
                'description': organization.description,
                'address': organization.address
            })
        return JsonResponse(data, safe=False)
