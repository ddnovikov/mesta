from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


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
        'main_form': form,
        'title': 'Создать пост',
        'submit_value': 'Создать пост',
    }

    return render(request, 'create_form.html', context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)

    context = {
        'instance': instance,
    }

    return render(request, 'posts_detail.html', context)


def post_list(request):
    all_posts_qs = Post.objects.all()
    search_query = request.GET.get('q')

    paginator = Paginator(all_posts_qs, 15)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': 'Блоги',
        'object_list': posts,
        'num_pages': range(1, posts.paginator.num_pages + 1),
    }

    return render(request, 'posts_list.html', context)


@login_required
def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,
                    request.FILES or None,
                    instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Успешно сохранено.')
        return redirect(instance)

    context = {
        'instance': instance,
        'main_form': form,
        'title': f'Редактировать пост {instance}',
        'submit_value': 'Сохранить изменения',
    }

    return render(request, 'create_form.html', context)


@login_required
def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, 'Успешно удалено.')

    return redirect('blogs:home')
