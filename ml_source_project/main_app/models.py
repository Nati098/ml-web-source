from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, blank=False)
    content = models.TextField(verbose_name='content', blank=False)  # https://stackoverflow.com/questions/4915397/django-blob-model-field/4915465
    date = models.DateField(verbose_name='public_date', blank=False)
    is_accepted = models.BooleanField(verbose_name='is_accepted', blank=False)

    def __str__(self):
        return self.title


class WebDemo(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, blank=False)
    content = models.TextField(verbose_name='content')  # https://stackoverflow.com/questions/4915397/django-blob-model-field/4915465
    code = models.TextField(verbose_name='code', blank=False)
    is_accepted = models.BooleanField(verbose_name='is_accepted', blank=False)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(models.Model):
    value = models.CharField(verbose_name='value', max_length=50, blank=False)

    def __str__(self):
        return self.value


class UserRole(models.Model):
    value = models.CharField(verbose_name='value', max_length=10, blank=False)

    def __str__(self):
        return self.value


class User(models.Model):
    login = models.CharField(verbose_name='login', max_length=20, blank=False)
    password = models.CharField(verbose_name='password', max_length=20, blank=False)
    email = models.EmailField(verbose_name='email', help_text='example@mail.ru', blank=False)
    fio = models.CharField(verbose_name='fio', max_length=30, blank=True)
    bday = models.DateField(verbose_name='bday', blank=True, null=True)

    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)  # поле отношений - сейчас: 1 ко многим
    favourites = models.ManyToManyField(Article)

    def __str__(self):
        return self.login
