from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.forms import SharingByEmailForm
from blog.models import Article


def article_list(request):
    object_list = Article.published.all()
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
                   'page': page})


def article_detail(request, year, month, day, article_slug):
    article = get_object_or_404(Article, slug=article_slug,
                                is_draft=False, publish__year=year,
                                publish__month=month, publish__day=day)

    return render(request, 'blog/article/detail.html', {'article': article})


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
