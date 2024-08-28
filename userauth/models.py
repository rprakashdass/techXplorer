from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, user_type=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username=username,
            password=password,
            user_type='admin'
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User_register(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ('test', 'Test'),
        ('dev', 'Developer'),
        ('student', 'Student'),
    )

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class UserInfo(models.Model):
    skills = (
        ("python", "Python"),
        ("sql" , "SQL"),
        ("software", "Software"),
        ("full stack", "Full stack developer"),
        ("front end", "Front End developer"),
    )
    user = models.OneToOneField(User_register, on_delete=models.CASCADE, related_name='info')
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    interested_domains = models.CharField(max_length=255, blank=True, null=True)
    followers = models.ForeignKey(User_register, on_delete=models.CASCADE, related_name='followers', null=True)
    following = models.ForeignKey(User_register, on_delete=models.CASCADE, related_name='following', null=True)
    skills = models.CharField(max_length=255, choices=skills, default=None)

    def __str__(self):
        return f'{self.user.username} - {self.user.user_type}'

class Hackathons(models.Model):
    author = models.ForeignKey(User_register, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    posted_location = models.CharField(max_length=255)
    posted_support = models.CharField(max_length=255)
    queries = models.TextField()
    demo_link = models.URLField(blank=True, null=True)
    post_image = models.ImageField(upload_to='hackathon_images/', blank=True, null=True)
    post_video = models.FileField(upload_to='hackathon_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class AiModels(models.Model):
    author = models.ForeignKey(User_register, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    posted_location = models.CharField(max_length=255)
    posted_support = models.CharField(max_length=255)
    queries = models.TextField()
    demo_link = models.URLField(blank=True, null=True)
    post_image = models.ImageField(upload_to='hackathon_images/', blank=True, null=True)
    post_video = models.FileField(upload_to='hackathon_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class ExploreApi(models.Model):
    author = models.ForeignKey(User_register, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    posted_location = models.CharField(max_length=255)
    posted_support = models.CharField(max_length=255)
    queries = models.TextField()
    demo_link = models.URLField(blank=True, null=True)
    post_image = models.ImageField(upload_to='hackathon_images/', blank=True, null=True)
    post_video = models.FileField(upload_to='hackathon_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption