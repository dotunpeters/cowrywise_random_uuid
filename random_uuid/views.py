from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import uuid
from datetime import datetime
import pytz


class Index(APIView):
    def get(self, request):
        current_datetime = str(datetime.now(tz=pytz.UTC))
        if "uuid" not in request.session.keys():
            result = request.session["uuid"] = {current_datetime: str(uuid.uuid4())}
        else:
            result = request.session["uuid"]
            result[current_datetime] = str(uuid.uuid4())
        request.session["uuid"] = result
        return Response(result, status=status.HTTP_200_OK)
