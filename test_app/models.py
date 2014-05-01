from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)

    #objects = TodayPostsManager()


class Group(models.Model):
    name = models.CharField(max_length=6)


class Student(models.Model):
    group = models.ForeignKey(Group)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
