import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OrgConfig, Contact


@api_view(['GET', 'POST'])
def simulate_response_on(request):
    org_url = OrgConfig.instance().callback_url
    data = {}
    for key in request.query_params:
        data[key] = request.query_params.get(key)
    for key in request.data:
        data[key] = request.data.get(key)
    message_id = data.get("id")
    contact_number = data.get("to") or data.get("to_no_plus")
    status = "Success"
    if contact_number:
        contact, _= Contact.objects.get_or_create(number=contact_number)
        response = contact.get_response()
    else:
        contact = None
        response = ""
        status = "Not enought of params"

    try:
        if message_id:
            requests.get(f"{org_url}/delivered", params={"id": message_id})
        if contact_number:
            requests.get(f"{org_url}/receive", params={"from": contact_number, "text": response})
    except:
        status = "Problems with sending callback. Check organization url."

    return Response({
        "id": message_id,
        "contact_number": contact_number,
        "org_url": org_url,
        "response": response,
        "status": status
    })
