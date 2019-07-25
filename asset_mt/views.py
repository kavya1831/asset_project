from __future__ import unicode_literals

import json
from models import AssetTable

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



def test_view(requests):
    print requests
    response = {"message": "API Working Successfully"}
    return JsonResponse(response)

@csrf_exempt
def asset_db_test(requests):
    if (requests.method == "GET"):
        response_obj = AssetTable.objects.all()
        response = {"data":[]}

        for element in response_obj:
            response["data"].append(

                {"asset_name":element.asset_name,"asset_room":element.asset_room,"asset_purchase_value":element.asset_pv}
            )


    elif (requests.method == "POST"):
        request_body = json.loads(requests.body)
        AssetTable.objects.create(**request_body)
        response = {"message": "POST method is Working Successfully"}
    elif (requests.method == "PUT"):
        response = {"message": "PUT method is Working Successfully"}
    else :
        response = {"message": "DELETE method is Working Successfully"}

    return JsonResponse(response)
