class BaseService(object):

    _repo = property(fget=lambda self: self.entity.objects)

    def __getattr__(self, name):
        """
            Delegates automatically all undefined methods on the repository entity.
        """
        def decorator(*args, **kwargs):

            method = getattr(self._repo, name)
            if method is None:
                raise AttributeError("'%s' has no attribute '%s'" % (self.__class__.__name__, name))

            if not kwargs.pop("without_filters", False):
                for key, value in self.default_query_params.iteritems():
                    kwargs.setdefault(key, value)

            return method(*args, **kwargs)

        return decorator

    def get_all(self):
        return self.all()

    def get_one(self, *args, **kwargs):
        objects = self.filter(*args, **kwargs)
        return objects[0] if objects else None

    def new(self, *args, **kwargs):
        new = self.entity(*args, **kwargs)
        new.save()
        return new

    def delete(self, *args, **kwargs):

        logical_delete = kwargs.pop("logical", False)

        objs = self.filter(*args, **kwargs)

        if not objs:
            return None

        for obj in objs:
            if not logical_delete:
                obj.delete()
            else:
                obj.active = False
                obj.save()

        return objs
