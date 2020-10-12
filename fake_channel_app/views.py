import requests

from django.shortcuts import render
from django.http import JsonResponse
from .models import OrgConfig, Contact


def simulate_response_on(request):
    org_url = OrgConfig.instance().callback_url
    message_id = request.GET.get("id")
    contact_number = request.GET.get("to") or request.GET.get("to_no_plus")
    contact, _= Contact.objects.get_or_create(number=contact_number)
    response = contact.get_response()
    status = "Success"

    try:
        requests.get(f"{org_url}/delivered", params={"id": message_id})
        requests.get(f"{org_url}/receive", params={"from": contact_number, "text": response})
    except:
        status = "Fail"

    return JsonResponse({
        "id": message_id,
        "contact_number": contact_number,
        "org_url": org_url,
        "response": response,
        "status": status
    })