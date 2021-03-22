from django.views.generic import ListView, DetailView, CreateView
from .models import Upload


class UploadListView(ListView):
    model = Upload
    template_name = 'upload_home.html'
    context_object_name = 'mes_images'
    # https://docs.djangoproject.com/fr/3.1/topics/class-based-views/generic-display/


class UploadDetailView(DetailView):  # new
    model = Upload
    template_name = 'image_detail.html'
    context_object_name = 'mon_image'


class UploadCreateView(CreateView):
    model = Upload
    template_name = 'upload_new.html'
    fields = ['title', 'image','author', 'body']


class HomePageView(ListView):
    model = Upload
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new

'''
import cloudinary, cloudinary.uploader, cloudinary.forms


class UploadFileForm(forms.Form):
    image  = cloudinary.forms.CloudinaryJsFileField()

def save(request):
    form = UploadFileForm(request.POST)
    cloudinary.forms.cl_init_js_callbacks(form, request)
    if request.method == 'POST':
        if form.is_valid():
            image = form.cleaned_data['image']
            return HttpResponseRedirect(image.url())
    return render_to_response('posts/upload.html', 
                              RequestContext(request, {'form': form, 'post': p}))
                              '''
