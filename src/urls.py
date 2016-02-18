from anillo.handlers.routing import optionized_url as url, context


from controllers.index import Index
from controllers.user import Login, Register, List

urls = [
    context("/api/v1", [
        url("/", Index(), methods=["get", "post"]),
        url("/login", Login(), methods=["post"]),
        url("/users", Register(), methods=["post"]),
        url("/users", List(), methods=["get"]),
    ]),
]
