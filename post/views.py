from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .models import Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils import timezone                  # bunun nedenide satış_date i çalıştırmak
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def post_index(request):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)  |
            Q(titleiki__icontains=query) |
            Q(content__icontains=query)  |
            Q(user__first_name__icontains=query) |
            Q(publishing_date__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    return render(request,'post/index.html',{'posts':posts})

def post_indexy(request):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            #Q(title__icontains=query)  |
            Q(titleiki__icontains=query)
            #Q(content__icontains=query)  |
            #Q(user__first_name__icontains=query) |
            #Q(publishing_date__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    return render(request,'post/indexy.html',{'posts':posts})


def post_indexsat(request):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        raise Http404()                                    # BURDA RAİSE KULLANDIK DİĞERLERİNDEN FARKLI
    posts = Post.objects.all()
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)  |
            Q(titleiki__icontains=query) |
            Q(content__icontains=query)  |
            Q(user__first_name__icontains=query) |
            Q(publishing_date__icontains=query)

        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'post/indexsat.html',{'posts':posts})

def post_indexsatrapor(request):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        raise Http404()                                    # BURDA RAİSE KULLANDIK DİĞERLERİNDEN FARKLI
    posts = Post.objects.all()
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
          #  Q(title__icontains=query)  |
            Q(esnaf__icontains=query) |
            Q(titleiki__icontains=query)
          # Q(content__icontains=query)  |
          #  Q(user__first_name__icontains=query) |
          #  Q(publishing_date__icontains=query)

        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'post/indexsatrapor.html',{'posts':posts})

def post_indexhurda(request):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        raise Http404()                                    # BURDA RAİSE KULLANDIK DİĞERLERİNDEN FARKLI
    posts = Post.objects.all()
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)  |
            Q(titleiki__icontains=query) |
            Q(content__icontains=query)  |
            Q(user__first_name__icontains=query) |
            Q(publishing_date__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'post/indexhurda.html',{'posts':posts})

def post_indexemanet(request):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        raise Http404()                                    # BURDA RAİSE KULLANDIK DİĞERLERİNDEN FARKLI
    posts = Post.objects.all()
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)  |
            Q(titleiki__icontains=query) |
            Q(content__icontains=query)  |
            Q(user__first_name__icontains=query) |
            Q(publishing_date__icontains=query)

        ).distinct()

    paginator = Paginator(post_list, 25)  # Show 25 contacts per page

    page = request.GET.get('Sayfa')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'post/indexemanet.html',{'posts':posts})


def post_detail(request, slug):
    post= get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None,)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context= {
        'post':post,
        'form':form,
    }
    return render(request,'post/detail.html',context)

def post_create(request):
    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        raise Http404()                                    # BURDA RAİSE KULLANDIK DİĞERLERİNDEN FARKLI
    form =PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)              #  commit=False    # bu veriyi kaydetmiyor artık içindekilerden dolayı ama doldurulan formu bize geri veriyo
        post.user = request.user

        post.save()
        # post.slug = slugify(post.titleiki.replace('ı','i'))                              # normali title ama o seri no veremeyiz diye model verdim isme
        # post.save()                                                            # şimdi kaydettik
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_update(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.save() #
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_updatedate(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.save() #
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/formdate.html', context)

def post_updateiadesat(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.kazanc = post.kacasatıldı - post.titleuc                    #post.kacasatıldı - post.titleuc   --------- post.topkaz = "0"post.topkaz = + post.kazanc
        post.save() #
        messages.success(request, 'Başarılı bir şekilde  satış oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/formiadesat.html', context)

def post_updateiadeem(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.save() #
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/formiadeem.html', context)

def post_updateiadehu(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.save() #
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/formiadehu.html', context)

def post_updateiade(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
       #form.save()
        post = form.save(commit=False)
        post.author = request.user
        post.satış_date = timezone.now()         # zamanı yeniliyor.. bu benim bok yemem :)
        post.save() #
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz.', extra_tags='mesaj-başarili')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post/formiade.html', context)

def post_delete(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                # BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')

def post_deletec(request, slug):
    if not request.user.is_authenticated():
        return Http404()
    comments = get_object_or_404(Comment, )      # HERBİR YORUMUN İD SİNİ BELİRTMELİYİZ BURDA..
    comments.delete()
    return redirect('post:index')





def post_deletex(request, slug):

    if not request.user.is_authenticated():              # UNUTMA BU GİZLİ SEKMENTDEN AÇILMAMASI İÇİN
        return Http404()                                #BURDA RAİSE DEĞİL RETURN KULLANDIK KULLANDIK DİĞERLERİNDEN FARKLI
    post = get_object_or_404(Post, slug=slug)
    post.kacasatıldı = "0"
    post.contents  = ""
    post.contente  = ""
    post.contenth  = ""
    post.kazanc = "0"                                 #   post.topkaz = post.topkaz - post.kazanc
    post.save() #
    return redirect('post:index')


def hello(request):
    return render(request, 'post/base.html', context)

#for post in post.satış_date.all