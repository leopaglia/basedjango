def dict_to_obj(dic):

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    return Struct(**dic)
