from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.
def index(request):
    reviews = Review.objects.all()[::-1]
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)


# def detail(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     context = {
#         'review': review,
#     }
#     return render(request, 'reviews/detail.html', context)