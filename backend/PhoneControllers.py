import json

from dependency_injector.wiring import inject, Provide
from flask import request, Response

from MainContainer import MainContainer
from ServiceException import ServiceException
from PhoneService import PhoneService


@inject
def api(phone_rep: PhoneService = Provide[MainContainer.phone_repository]):
    phone_number = request.args.get("phoneNumber", default="", type=str)
    r = Response()
    r.headers["Access-Control-Allow-Origin"] = "*"
    r.headers["Access-Control-Allow-Headers"] = "*"
    r.headers["Access-Control-Allow-Methods"] = "*"

    if len(str(int(phone_number))) != 10:
        r.status = 422
    try:
        res = phone_rep.get_data(phone_number)
        if res[1] is None or res[2] is None:
            r.status = 422
        else:
            r.response = [json.dumps({"original_provider": res[0], "current_provider": res[1], "region": res[2]})]
    except ServiceException:
        r.status = 400
    return r
