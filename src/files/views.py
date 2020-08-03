from django.shortcuts import redirect
from django.http.response import Http404, HttpResponse
from .models import Version


def get_direct_link(request, hashid):
    try:
        version = Version.dehashid(hashid)
    except IndexError:
        raise Http404
    file = version.file

    return redirect('/download/%s/%s' % (version.slug, file.name), permanent=True)
