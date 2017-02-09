---
title: Quick review making django working with heroku
date: 2014-07-30
category: sysadmin
tags: aRkadeFR, heroku, django
slug: quick-review-making-django-working-with-heroku
author: aRkadeFR
summary: After being tired of doing some sysadmin, I chose to migrate 1avis.fr to heroku.
---

# Hey Pony lovers! #

After doing some very interesting sysadmin with Debian, LXC, etc. I was, sadly,
confronted to common problems about third services (email, file system etc.).

Because I'm slow on the project 1avis.fr, I decided to migrate to some robust,
and approved system from Django community.

## Today, we migrate to [heroku](http://heroku.com/)! ##

Heroku is a SaaS, that already has some Django applications working on. It uses
LXC, Gunicorn etc. cedar stack for django!

## My feeling about it after 2 days ##

I successfully deployed a Django applicatoin, with the common features (static
file on AWS S3, email handled by gmail…). It was very easy, the documentation is
clear and simple, and the community is already pretty big.

## If you're a dev heroku is a great tool ##

I really like deploying a Django application to heroku, and feeling secure about
all the common tasks: backup of the databases, supervisor of services…

I spent most of my time into my settings.py, but to the end, I have no
difference between my production environment, and my development environment,
thanks to virtualenv, and pip :)
