from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import AuthorRegistrationForm, CommentForm
from .models import Author, Comment
from django.contrib.auth.models import User


def register_author(request):
    if request.method == 'POST':
        form = AuthorRegistrationForm(request.POST)
        if form.is_valid():
            # Создаем пользователя Django
            user = User.objects.create_user(username=form.cleaned_data['name'], password=form.cleaned_data['password'])

            # Создаем автора и привязываем к пользователю
            author = Author.objects.create(user=user, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            author.save()
            login(request, user)  # Логиним пользователя после регистрации
            return redirect('success')  # Перенаправляем на страницу успеха
    else:
        form = AuthorRegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')  # Перенаправление поменять
        else:
            # Обработка неверных учетных данных, например, вывод сообщения об ошибке
            pass

    return render(request, 'login.html')


def success_view(request):
    comments = Comment.objects.all()  # Получаем все комментарии

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(user=request.user)  # Получаем текущего автора
            content = form.cleaned_data['content']
            parent_comment_id = form.cleaned_data.get('parent_comment_id')  # Если нужно, можно добавить поле для ответа на определенный комментарий

            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                comment = Comment.objects.create(author=author, content=content, parent_comment=parent_comment)
            else:
                comment = Comment.objects.create(author=author, content=content)

            comment.save()
            return redirect('success')  # Перенаправляем на страницу успеха после добавления комментария
    else:
        form = CommentForm()

    return render(request, 'success.html', {'comments': comments, 'form': form})