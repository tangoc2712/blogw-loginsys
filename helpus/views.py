from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContributeRegisterForm
from accounts.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import SignVideoUpload

# Create your views here.
def register_contribute(request):
    welldone = False
    welldone1 = False
    if request.user.is_contribute:
        welldone1 = True
    if request.method == "POST":
        # Form was submitted
        form = ContributeRegisterForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = (
                form.cleaned_data
            )  # la dictionary chứa dữ liệu clear, chỉ gọi được sau khi check is_valid
            print("data: ", cd)
            user = get_object_or_404(User, email=request.user)
            user.fullname = cd['fullname']
            user.phone = cd['phone']
            user.facebook = cd['facebook']
            user.status_contribute = True
            user.save()
            welldone = True
    else:
        form = ContributeRegisterForm()
    

    contexts = {
        "form": form,
        "welldone": welldone,
        "welldone1": welldone1,
    }
    return render(request, "helpus/register_contribute.html", contexts)

def contribute(request):
    print(request.user.is_contribute)
    welldone = False
    if request.user.is_contribute:
        welldone = True
    if request.method == 'POST':
        word = request.POST['word']
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        file_name = fs.save(name=upload_file.name, content=upload_file)
        path = settings.MEDIA_ROOT + file_name
        user = get_object_or_404(User, email=request.user)

        new_instance = SignVideoUpload.objects.create(word=word, video=path, contributor=user)
        print(path, word)

    contexts = {
        "welldone": welldone,
    }
    return render(request, "helpus/contribute.html", contexts)