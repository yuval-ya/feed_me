from django.apps import AppConfig


class FeedConfig(AppConfig):
    name = 'feed'
    verbose_name = ' Posts, Comments, Likes'

    def ready(self):
        import feed.signals    #noqa