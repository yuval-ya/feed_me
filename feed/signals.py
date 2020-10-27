from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Post, Like
from os import remove


@receiver(post_save, sender=Like)
def post_save_post_liked(sender, instance, **kwargs):
    sender_ = instance.user
    receiver_ = instance.post
    receiver_.liked.add(sender_)
    receiver_.save()


@receiver(pre_delete, sender=Like)
def pre_delele_post_unliked(sender, instance, **kwargs):
    sender_ = instance.user
    receiver_ = instance.post
    receiver_.liked.remove(sender_)
    receiver_.save()
