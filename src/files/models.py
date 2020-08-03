from django.db.models import *
from random import choices
from string import ascii_letters, digits
from os.path import join

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


def upload_version_to(instance, filename):
    return join(instance.slug, instance.file.name)


class Version(Model):
    file = ForeignKey(File, on_delete=CASCADE, related_name='versions')
    name = CharField(max_length=100)
    content = FileField(upload_to=upload_version_to)
    slug = CharField(unique=True, default=slug, max_length=20)

    @property
    def hashid(self):
        return self.id and hashids.encode(self.id)

    @classmethod
    def dehashid(cls, hashid):
        return Version.objects.get(id=hashids.decode(hashid)[0])

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Version %s>" % self.__str__()
