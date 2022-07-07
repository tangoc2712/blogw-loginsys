from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib import messages
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm, CreateUserForm
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .decorators import unauthenticated_user

# Create your views here.

# ================Class-based-view===============================

@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = "blog/post/list.html"


# ===============================================================

# ================Fucntion-based-view============================

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 2)
#     page = request.GET.get("page")

#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:  # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:  # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request, "blog/post/list.html", {"page": page, "posts": posts})

#     # with HttpResponse
#     # template = loader.get_template("blog/post/list.html")
#     # context = {"posts": posts}
#     # return HttpResponse(template.render(context, request))

# ===============================================================

@login_required
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    # Lấy ra đống comment đã active,
    # dùng như này là vì ở Comment model có relate đến Post
    # dưới cái tên là comments,
    # nên coi nó là đối tượng thông qua để lấy thuộc tính active
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == "POST":  # nếu thông tin đã được gửi
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(
                commit=False
            )  # tạo Comment object, nhưng thiếu thuộc tính post
            new_comment.post = post  # thêm thuộc tính post
            new_comment.save()  # lưu vào CSDL
    else:
        comment_form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "blog/post/detail.html", context)

@login_required
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status="published")
    sent = False
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = (
                form.cleaned_data
            )  # la dictionary chứa dữ liệu clear, chỉ gọi được sau khi check is_valid
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(subject, message, "taquangngoc.hh31@gmail.com", [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()

    context = {
        "post": post,
        "form": form,
        "sent": sent,
    }
    return render(request, "blog/post/share.html", context)

@login_required
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
        results = Post.published.annotate(
            search=SearchVector("title", "body"),
        ).filter(search=query)

    context = {
        "query": query,
        "form": form,
        "results": results,
    }
    return render(request, "blog/post/search.html", context)

@login_required
def model_predict(request):
    context = {}
    return render(request, "blog/post/model.html", context)