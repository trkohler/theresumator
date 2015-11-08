from django.db import models
from solo.models import SingletonModel
from django.utils.translation import ugettext_lazy as _


class BasicInformation(SingletonModel):
    name = models.CharField(max_length=25, default="John Smith")
    short_bio = models.CharField(max_length=100,
                                 blank=True,
                                 verbose_name=_("short bio"),
                                 default="My short bio")
    long_bio = models.TextField(blank=True,
                                verbose_name=_("long bio"),
                                default="My long bio")
    email = models.EmailField(default="email@example.com")
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    image = models.ImageField(null=True)

    def __repr__(self):
        return '<BasicInformation: %s>' % self.name

    def __str__(self):
        return self.name.title()


class Education(models.Model):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=10, blank=True, default=None)
    abbreviation = models.CharField(max_length=10, blank=True, default=None)
    major = models.CharField(max_length=15, blank=True, default=None)
    gpa = models.CharField(max_length=10, blank=True, default=None)

    def __repr__(self):
        return '<Education: %s>' % self.name

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=50)
    Authors = models.CharField(max_length=100, blank=True, default=None)
    venue = models.CharField(max_length=20, blank=True, default=None)
    year = models.CharField(max_length=4, blank=True, default=None)
    link = models.URLField(null=True, blank=True)

    def __repr__(self):
        return '<Publication: %s>' % self.name

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=None,
                                   blank=True,
                                   verbose_name=_("description"))
    link = models.URLField()
    picture = models.ImageField()

    def __repr__(self):
        return '<Project: %s>' % self.name

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=150)
    start_date = models.DateField(verbose_name=_("start date"))
    end_date = models.DateField(verbose_name=_("end date"))
    description = models.TextField(default=None,
                                   verbose_name=_("description"))
    URL = models.URLField(null=True, blank=True)

    def __repr__(self):
        return '<Experience: %s>' % self.company

    def __str__(self):
        return '%s at %s' % (self.role.capitalize(), self.company)


class Language(models.Model):
    name = models.CharField(max_length=20)
    experience = models.ForeignKey(Experience, null=True, blank=True, default=None)
    projects = models.ForeignKey(Project, null=True, blank=True, default=None)

    def __repr__(self):
        return '<Language: %s>' % self.name

    def __str__(self):
        return self.name
