from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from users.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts_pics', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True)
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author.user}'s post from {self.date_posted}"

    def get_likes_num(self):
        return self.liked.all().count()

    def get_profiles_liked(self):
        return self.liked.all()

    def get_comments_num(self):
        return self.comment_set.all().count()

    def get_absolute_url(self):
        return reverse('post-update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('-date_posted',)


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author}'s comment on {self.post.author} post"

    class Meta:
        ordering = ('-created',)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} Liked {self.post}"
