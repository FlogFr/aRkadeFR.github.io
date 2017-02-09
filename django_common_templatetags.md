---
title: Django templatetags and DRY
date: 2014-10-18
category: django
tags: aRkadeFR, django, app
slug: django-common-templatetags-application
author: aRkadeFR
summary: common templatetags reusable over apps
---

If you're new to templatetags, please read the [documentation](https://docs.djangoproject.com/en/1.7/ref/templates/builtins/).
And how the [documentation](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/)
on custom templatetags.

# Template tags are boring. DRY

Template tags are boring to write, you have a context, and you either need to
change it or render a string to your template. Most of the time, these
templatetags can be completely generic.

# Example my dear ?

The only one in the package so far is 'url\_change\_param'. Which take the
current request.path and the current querydict to return the exact same one
except you can add or change a value to the querydict.

This is pretty awesome when you have a paginated page, with multiple params like
'page\_size', 'page', 'filter\_XX' etc. And you need to change only the page
number :)

# State of the art of the package

Brand new package, but already available on the Cheese Shop thanks to setuptools
:) you can read the documentation on [pythonhosted](https://pythonhosted.org/django-common-templatetags/).

I would be extremely happy if you contribute to the package. Please ask for git
pull on the [github project](https://github.com/aRkadeFR/django-common-templatetags).
