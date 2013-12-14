from django.db import models

class PubFig(models.Model):
  name = models.CharField(max_length=255)
  image_url = models.URLField()

  def __unicode__(self):
    return self.name


class Statement(models.Model):
    pubfig = models.ForeignKey(PubFig)
    quote = models.TextField()
    date = models.DateField()
    about = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    source_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
      return self.quote[:10] + "..."
