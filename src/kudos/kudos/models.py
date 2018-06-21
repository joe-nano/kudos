from django.db import models


class Kudo(models.Model):
  from_person = models.TextField()
  to_person = models.TextField()
  created = models.DateTimeField(auto_now_add=True, blank=True)
  text = models.TextField()
