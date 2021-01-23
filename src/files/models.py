from django.db.models import *
from random import choices
from string import ascii_letters, digits
from os.path import join

from django.utils.functional import cached_property
from hashids import Hashids

hashids = Hashids(salt='7c1ba8fdc91012d6edb7190955c769b84a83c3922a53f2f9fbfe8981e22a430f515cdd42e307427a',
                  min_length=11)


def slug():
    return ''.join(choices(ascii_letters+digits, k=20))


class File(Model):
    name = CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<File %s>" % self.__str__()

    @cached_property
    def latest_version(self):
        return self.versions.filter(is_latest=True).first()


def upload_version_to(instance, filename):
    return join(instance.slug, instance.file.name)


class Version(Model):
    file = ForeignKey(File, on_delete=CASCADE, related_name='versions')
    name = CharField(max_length=100)
    content = FileField(upload_to=upload_version_to)
    slug = CharField(unique=True, default=slug, max_length=20)
    is_latest = BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            latest = self.file.latest_version
            if latest:
                latest.is_latest = False
                latest.save()
        super().save(force_insert, force_update, using, update_fields)


    @property
    def hashid(self):
        return self.id and hashids.encode(0, self.id)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Version %s>" % self.__str__()


def dehashid(hashid):
    hashtype, id = hashids.decode(hashid)
    if hashtype == 0:
        return Version.objects.filter(id=id).first(), True
    else:
        return File.objects.filter(id=id).first(), False


class Alias(Model):
    slug = CharField(unique=True, max_length=255)
    target_version = ForeignKey(Version, on_delete=CASCADE, null=True, blank=True)
    target_file = ForeignKey(File, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.slug

    def __repr__(self):
        return "<Alias %s>" % self.__str__()