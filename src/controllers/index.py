from anillo.http import Ok

from .controller import Controller

import logging

class Index(Controller):
    def get(self, request):
        logging.info("[GET] Index")
        return Ok({"message": "Welcome to this API.", "api-version": "1.0"})

    def post(self, request):
        return Ok({"message": "Welcome to this API.", "api-version": "1.0"})
