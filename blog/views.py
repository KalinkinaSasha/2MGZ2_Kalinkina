
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def post(request, post_id):
    return render(
        request,
        'blog/post.html',
        {'post_id': post_id}
    )


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    published_reviews = Review.objects.filter(is_checked=True)

    return render(request, 'blog/reviews.html', {
        'form': form,
        'reviews': published_reviews
    })
