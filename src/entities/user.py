from .entity import Entity

class User(Entity):
    def __init__(self, *args, **kwargs):
        self.email = kwargs['email']
        self.password = kwargs['password']
        self.uuid = kwargs['uuid']

    def __repr__(self):
        return "entities.User: {}".format(self.email)

    def toJSONDict(self):
        return super(User, self).toJSONDict(["uuid", "email"])
