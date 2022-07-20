from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContributeRegisterForm
from accounts.models import User
# Create your views here.
def register_contribute(request):
    welldone = False
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
    }
    return render(request, "helpus/register_contribute.html", contexts)

def contribute(request):
    contexts = {}
    return render(request, "helpus/register_contribute.html", contexts)