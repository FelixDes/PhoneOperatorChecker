from dependency_injector.wiring import inject, Provide
from flask import request

from backend.MainContainer import MainContainer
from backend.services.PhoneRepository import PhoneRepository


@inject
def index(phone_rep: PhoneRepository = Provide[MainContainer.phone_repository]):
    phone_number = request.args.get("phoneNumber", default="", type=str)
    print(phone_rep.pg_pool)
    return phone_rep.get_provider(phone_number)
