from django.db import models


class Zombie(models.Model):
    name_zombie = models.CharField(max_length=40)
    cementery = models.CharField(max_length=40)

    def __unicode__(self):
        return 'Zombie: %s - %s' % (self.pk, self.name_zombie,)


class Tweet(models.Model):
    status = models.CharField(max_length=140)
    zombie = models.ForeignKey('Zombie', related_name='tweetss')
    created_at = models.DateTimeField(auto_now_add=True)
