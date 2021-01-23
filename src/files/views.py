from django.shortcuts import redirect
from django.http.response import Http404
from .models import Alias, dehashid


def get_version(hashid):
    alias = Alias.objects.filter(slug=hashid).first()
    if alias:
        target_version = alias.target_version
        target_file = alias.target_file
        if target_version:
            return target_version
        elif target_file:
            latest_version = target_file.latest_version
            if latest_version:
                return latest_version
    try:
        instance, is_version = dehashid(hashid)
    except (IndexError, ValueError):
        raise Http404
    if not is_version:
        instance = instance.latest_version
    if not instance:
        raise Http404
    return instance


def get_download_link(request, hashid):
    version = get_version(hashid)
    file = version.file

    return redirect('/uploads/%s/%s' % (version.slug, file.name), permanent=True)


def get_view_link(request, hashid):
    version = get_version(hashid)
    file = version.file

    return redirect('/view/%s/%s' % (version.slug, file.name), permanent=True)
