from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Photo, Category, Icon
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm, IconForm
from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'photos': photos})


def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {
        'user': user,
        'photos': photos,
    })


@login_required
def photos_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, "投稿が完了しました！")
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
    return render(request, 'app/photos_new.html', {'form': form})


def photos_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/photos_detail.html', {'photo': photo})


@require_POST
def photos_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('app:users_detail', request.user.id)


def photos_category(request, category):
    category = Category.objects.get(title=category)
    photos = Photo.objects.filter(category=category).order_by('-created_at')
    return render(request, 'app/index.html', {'photos': photos, 'category':category})


@login_required
def icon_new(request):
    if request.method == "POST":
        form = IconForm(request.POST, request.FILES)
        if form.is_valid():
            # 既存のアイコンを削除
            Icon.objects.filter(user=request.user).delete()
            # 新しいアイコンを保存
            icon = form.save(commit=False)
            icon.user = request.user
            icon.save()
            messages.success(request, "投稿が完了しました！")
        return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = IconForm()
    return render(request, 'app/icon_new.html', {'form': form})
