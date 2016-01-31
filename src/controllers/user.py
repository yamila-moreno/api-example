from anillo.http import Ok, BadRequest

from controllers.controller import Controller
from services.user import login, register, list
from utils.authorization import login_required
from validators.user import LoginValidator, RegisterValidator
from validators.validator import with_validators

class List(Controller):
    @login_required
    def get(self, request):
        success, result, errors = list()

        if errors:
            return BadRequest(errors)

        return Ok({'users': [u.toJSONDict() for u in result['users']]})

class Login(Controller):
    @with_validators([LoginValidator])
    def post(self, request, data):
        success, result, errors = login(
                data["login_data"].email,
                data["login_data"].password
        )

        if errors:
            return BadRequest(errors)

        return Ok(result)


class Register(Controller):
    @with_validators([RegisterValidator])
    def post(self, request, data):
        success, result, errors = register(
                data["register_data"].email,
                data["register_data"].password
        )

        if errors:
            return BadRequest(errors)

        return Ok({"user": result["user"].toJSONDict()})



