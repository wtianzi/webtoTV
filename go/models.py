from django.db import models

# Create your models here.
from django.db import models


class WebURL(models.Model):
    weburl_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.weburl_text)

class WordUnknown(models.Model):
    id=models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False,
                  verbose_name ='ID'
                )
    eng_word = models.CharField(max_length=300)
    chi_word = models.CharField(max_length=500)
    tag = models.BooleanField()
    def __str__(self):
        return str(self.eng_word)
