import base64
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User


class Article(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, blank=False)
    content = models.TextField(verbose_name='content', blank=False)  # https://stackoverflow.com/questions/4915397/django-blob-model-field/4915465
    date = models.DateField(verbose_name='public_date', blank=False)
    is_accepted = models.BooleanField(verbose_name='is_accepted', blank=False)

    models.ManyToManyField(User, blank=True, null=True)

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.title


class WebDemo(models.Model):
    title = models.CharField(verbose_name='title', max_length=100, blank=False)
    content = models.TextField(verbose_name='content')  # https://stackoverflow.com/questions/4915397/django-blob-model-field/4915465
    code = models.TextField(verbose_name='code', blank=False)
    date = models.DateField(verbose_name='public_date', blank=False)
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


# class User(AbstractUser):
#     fio = models.CharField(verbose_name='fio', max_length=30, blank=True)
#     bday = models.DateField(verbose_name='bday', blank=True, null=True)
#
#     role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, blank=True, null=True)  # поле отношений - сейчас: 1 ко многим
#     favourites = models.ManyToManyField(Article, blank=True, null=True)
#     date_joined = models.DateTimeField(default=timezone.now)


# class UserManager(BaseUserManager):
#     def create_user(self, login, email, password=None):
#         """
#         Creates and saves a User with the given login, email and password.
#         """
#         if not login:
#             raise ValueError('Users must have an login')
#         if not email:
#             raise ValueError('Users must have an email')
#
#         user = self.model(
#             login=login,
#             email=self.normalize_email(email)
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_staffuser(self, login, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             login=login,
#             email=email,
#             password=password,
#         )
#         user.staff = 2
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, login, password):
#         """
#         Creates and saves a superuser with the given login, email and password.
#         """
#         user = self.create_user(
#             login=login,
#             email="chicken000@mail.ru",
#             password=password,
#         )
#         user.staff = 0
#         user.admin = True
#         user.save(using=self._db)
#         return user


# class User(models.Model):
#     login = models.CharField(verbose_name='login', max_length=20, blank=False)
#     password = models.CharField(verbose_name='password', max_length=20, blank=False)
#     email = models.EmailField(verbose_name='email', help_text='example@mail.ru', blank=False)
#     fio = models.CharField(verbose_name='fio', max_length=30, blank=True)
#     bday = models.DateField(verbose_name='bday', blank=True, null=True)
#
#     role = models.ForeignKey(UserRole, on_delete=models.CASCADE)  # поле отношений - сейчас: 1 ко многим
#     favourites = models.ManyToManyField(Article)
#
#     def __str__(self):
#         return self.login
