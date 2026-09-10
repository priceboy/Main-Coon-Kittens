from django.views.generic import DetailView, ListView
from .models import Breed, Kitten

class KittenListView(ListView):
    model = Kitten
    template_name = "kittens/list.html"
    context_object_name = "kittens"
    paginate_by = 12
    def get_queryset(self):
        qs = Kitten.objects.filter(status="available").select_related("breed").prefetch_related("photos")
        if breed := self.request.GET.get("breed"): qs = qs.filter(breed_id=breed)
        if gender := self.request.GET.get("gender"): qs = qs.filter(gender=gender)
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breeds"] = Breed.objects.all()
        context["selected_breed"] = self.request.GET.get("breed", "")
        context["selected_gender"] = self.request.GET.get("gender", "")
        return context

class KittenDetailView(DetailView):
    model = Kitten
    template_name = "kittens/detail.html"
    context_object_name = "kitten"
