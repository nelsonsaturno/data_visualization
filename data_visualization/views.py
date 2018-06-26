from django.views.generic import TemplateView
from datetime import datetime
import requests


class IndexPricesView(TemplateView):
    template_name = 'index_prices.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        response = requests.get('http://127.0.0.1:8000/calculator/get-index-prices').json()
        dates = [datetime.strptime(d, "%Y-%m-%d") for d in response.keys()]
        dates.sort()
        context['dates'] = []
        context['prices'] = []
        for d in dates:
            context['dates'] += [str(d.date())]
            context['prices'] += [response[str(d.date())]]
        return self.render_to_response(context)
