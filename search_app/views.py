from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from search_app.models import Index
from search_app.forms import IndexForm
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, FormView

# Create your views here.
"""
class SearchView(View):
    def get(self, request):
        form = IndexForm()
        return render(request, 'search_app/search_page.html', {
            "form": form
        })

    def post(self, request):
        form = IndexForm(request.POST)

        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "search_app/search_page.html", {
            'form': form
        })

"""

""" class SearchView(CreateView):
    model = Index
    fields = '__all__' """

class SearchView(FormView):
    template_name = 'search_app/search_page.html'
    form_class = IndexForm
    success_url = '/thank-you'

    def form_valid(self, form):
        index_object = Index.objects.all()
        
        for index in index_object:
            print(index.id)
            if index.link == form.cleaned_data['link']:
                return HttpResponseRedirect("/error.html")
                break

        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "search_app/thank_you.html"


class ErrorView(TemplateView):
    template_name = "search_app/error.html"


"""
        if form.cleaned_data['title'] in Index.objects.all():
            print("Exist")
        else:
            print("doesn't exist")

        for index in index_object:
            if index.title == form.cleaned_data['title']:
                print("exist")
            else:
                print("doesn't exist")
            
            pass
            #print(index.link)
        print(form.cleaned_data['title'])
"""