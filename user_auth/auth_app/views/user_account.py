from django.http import JsonResponse
from django.views import View
import json
from ..models.user_account import UserAccount


class CreateUserAccountView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        if not email:
            return JsonResponse({'errors': 'Email is required'}, status=400)

        if UserAccount.objects.filter(email=email).exists():
            return JsonResponse({'errors': 'User with this email already exists'}, status=400)

        user_account = UserAccount(email=email, password=password, firstname=firstname, lastname=lastname)
        user_account.save()

        return JsonResponse({'user_account': {'id': str(user_account.id), 'email': user_account.email, 'firstname': user_account.firstname, 'lastname': user_account.lastname}}, status=201)


class ListUserAccountView(View):
    def get(self, request, user_id, *args, **kwargs):
        try:
            user_account = UserAccount.objects.get(id=user_id)
            return JsonResponse({'user_account': {'id': str(user_account.id), 'email': user_account.email, 'firstname': user_account.firstname, 'lastname': user_account.lastname}}, status=200)
        except UserAccount.DoesNotExist:
            return JsonResponse({'errors': 'User Account not found'}, status=404)
