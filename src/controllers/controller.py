from anillo.http import responses


class Controller:
    def __call__(self, request, *args, **kwargs):
        if request.method == "GET" and hasattr(self, 'get'):
            return self.get(request, *args, **kwargs)
        elif request.method == "POST" and hasattr(self, 'post'):
            return self.post(request, *args, **kwargs)
        elif request.method == "PUT" and hasattr(self, 'put'):
            return self.put(request, *args, **kwargs)
        elif request.method == "DELETE" and hasattr(self, 'delete'):
            return self.delete(request, *args, **kwargs)
        elif request.method == "PATCH" and hasattr(self, 'patch'):
            return self.patch(request, *args, **kwargs)
        elif request.method == "OPTIONS":
            return responses.Ok()
        return responses.MethodNotAllowed()
