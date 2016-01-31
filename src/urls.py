from anillo.handlers.routing import url

from controllers.index import Index
from controllers.user import Login, Register, List

urls = [
    url("/api/v1/", Index(), methods=["get", "post", "options"]),
    url("/api/v1/login", Login(), methods=["post", "options"]),
    url("/api/v1/users", Register(), methods=["post", "options"]),
    url("/api/v1/users", List(), methods=["get", "options"]),
]
