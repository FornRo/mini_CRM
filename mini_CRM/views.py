from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'customer_info/list.html'

    def get(self, rq):
        return render(rq, self.template_name)

