from dependency_injector.wiring import inject, Provide
from flask import request, Response

from backend.MainContainer import MainContainer
from backend.exceptions.ServiceException import ServiceException
from backend.services.PhoneService import PhoneService


@inject
def index(phone_rep: PhoneService = Provide[MainContainer.phone_repository]):
    phone_number = request.args.get("phoneNumber", default="", type=str)
    if len(str(int(phone_number))) != 10:
        return Response(status=422)
    try:
        res = phone_rep.get_provider(phone_number)
        return Response(response=res, status=200)
    except ServiceException:
        return Response(status=400)
