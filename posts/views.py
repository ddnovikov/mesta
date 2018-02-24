from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from posts.forms import PostForm
from posts.models import Post


@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Пост успешно создан.')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
        'title': 'Создать пост',
        'submit_value': 'Создать пост',
    }

    return render(request, 'shared/create_form.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)

    context = {
        'instance': instance,
    }

    return render(request, 'post_detail.html', context)


def post_list(request):
    all_posts_qs = Post.objects.active()
    search_query = request.GET.get('q')

    paginator = Paginator(all_posts_qs, 15)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'posts': posts
    }

    return render(request, 'post_list.html', context)


@login_required
def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Успешно сохранено.')
        return redirect(instance)

    context = {
        'instance': instance,
        'form': form,
        'title': 'Редактировать пост',
        'submit_value': 'Сохранить изменения',
    }

    return render(request, 'shared/create_form.html', context)


@login_required
def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Успешно удалено.')

    return redirect('posts:home')
