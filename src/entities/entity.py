class Entity:
    def toJSONDict(self, list):
        d = dict()
        for a, v in self.__dict__.items():

            if "{}".format(a) in list:
                d[a] = self._processValue(v)
        return d


    def _processValue(self, v):
        if (isinstance(v, Entity)):
            return v.toJSONDict()
        elif (isinstance(v, list)):
            l = []
            for val in v:
                l.append(self._processValue(val))
            return l
        else:
            return v
