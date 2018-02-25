from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from elasticsearch_dsl import Q

from mesta.helpers_and_misc.tools.chain_search import chain_search

from .documents import PostDocument
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

    paginator = Paginator(all_posts_qs, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': 'Блоги',
        'object_list': posts,
        'num_pages': range(1, posts.paginator.num_pages + 1),
    }

    return render(request, 'posts_list.html', context)


def post_search(request):
    search_query = request.GET.get('q')

    if search_query:
        search_results = chain_search(
            query_type_or_q=Q({"multi_match": {"query": search_query,
                                               "fields": ["title", "content", "tags"]}}),
            search_obj=PostDocument.search()
        )
        search_results = search_results.to_queryset()
        print(search_results)
    else:
        return HttpResponse('Задан пустой поисковый запрос.')

    context = {
        'object_list': search_results,
        'title': f'Результаты поиска по запросу "{search_query}"',
    }

    return render(request, 'posts_list.html', context=context)


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
