from django.conf import settings
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from taggit.models import Tag

from blog.forms import SharingByEmailForm, CommentForm, ArticleSearchForm
from blog.models import Article


def article_list(request, tag_slug=None):
    object_list = Article.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/article/list.html',
                  {'articles': articles,
                   'page': page,
                   'tag': tag})


def article_detail(request, year, month, day, article_slug):
    article = get_object_or_404(Article, slug=article_slug,
                                is_draft=False, publish__year=year,
                                publish__month=month, publish__day=day)

    comments = article.comments.filter(active=True)

    # Similiar articles
    article_tags_ids = article.tags.values_list('id', flat=True)
    similiar_articles = Article.published.filter(tags__in=article_tags_ids)\
        .exclude(id=article.id)

    return render(request,
                  'blog/article/detail.html',
                  {'article': article,
                   'total_comments': comments.count,
                   'similiar_articles': similiar_articles,})


def article_share(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_draft=False)
    is_sent = False

    if request.method == 'POST':
        form = SharingByEmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            article_url = request.build_absolute_uri(article.get_absolute_url())
            subject = f"{data['name']} recomends you read " \
                      f"{article.title}"
            message = f"Read {article.title} at {article_url}\n\n" \
                      f"{data['name']}'s comments: {data['message']}"

            send_mail(subject,
                      message,
                      settings.EMAIL_YOU,
                      [data['to']])

            is_sent = True
    else:
        form = SharingByEmailForm()

    return render(request, 'blog/article/share.html',
                  {'article': article,
                   'form': form,
                   'is_sent': is_sent})


def article_search(request):
    form = ArticleSearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = ArticleSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Article.published.annotate(
                search=SearchVector('title', 'content',)
            ).filter(search=query)

    return render(request, 'blog/article/search.html', {'form': form,
                                                        'query': query,
                                                        'results': results})


def comment_list(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    object_list = article.comments.filter(active=True)

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/comment/list.html',
                  {'total_comments': object_list.count,
                   'comments': comments,
                   'page': page,
                   'article': article})


def comment_create(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        comment = form.save(commit=False)
        comment.article = article
        comment.save()

        return redirect('blog:comment_list', article_slug=article.slug)

    else:
        form = CommentForm()

    return render(request, 'blog/comment/create.html',
                  {'article': article,
                   'form': form})
