from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone


class LandingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ['home']  # только главная страница

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return timezone.now()


