from django.shortcuts import render
from .models import NationalID
from .forms import SearchForm

# Create your views here.

def search(request):
    form = SearchForm(request.GET or None)

    if form.is_valid():
        national_id = form.cleaned_data['national_id']
        try:
            result = NationalID.objects.get(national_id=national_id)
            return render(request, 'search/download.html', {'result': result})
        except NationalID.DoesNotExist:
            form.add_error('national_id', 'شماره ملی پیدا نشد.')

    return render(request, 'search/search.html', {'form': form})