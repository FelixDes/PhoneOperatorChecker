from dependency_injector.wiring import inject, Provide
from flask import request, Response

from backend.MainContainer import MainContainer
from backend.exceptions.ServiceException import ServiceException
from backend.services.PhoneService import PhoneService


@inject
def index(phone_rep: PhoneService = Provide[MainContainer.phone_repository]):
    phone_number = request.args.get("phoneNumber", default="", type=str)
    r = Response()
    r.headers["Access-Control-Allow-Origin"] = "*"
    r.headers["Access-Control-Allow-Headers"] = "*"
    r.headers["Access-Control-Allow-Methods"] = "*"

    if len(str(int(phone_number))) != 10:
        r.status = 422
        return r
    try:
        res = phone_rep.get_provider(phone_number)
        r.response = str(res)
        return r
    except ServiceException:
        r.status = 400
        return r
