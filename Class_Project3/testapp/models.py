from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=30)
    ceo = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk': self.pk})
