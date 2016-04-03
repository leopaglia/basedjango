from .base import BaseView, AjaxView
from app.services.OneModelService import OneModelService


class OneView(AjaxView):

    def post(self, request):
        mah_data = request.POST.get('some_data', None)
        return self.success_response(lol='lololol', moar_data=mah_data)


class AnotherView(BaseView):

    def get(self, request, *args, **kwargs):

        asd = request.GET.get('asd')

        models = OneModelService().get_all()
        names = [obj.name for obj in models]

        context = {
            'data': '',
            'moar_data': '',
            'asd': asd,
            'names': names
        }

        return self.render_to_response(context)
