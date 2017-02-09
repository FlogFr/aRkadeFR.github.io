---
title: Django application Debian packaging for deployment
date: 2014-06-27
category: django
tags: aRkadeFR, Django, sysadmin, Debian, packaging, deployment
slug: Django-application-Debian-packaging-for-deployment
author: aRkadeFR
summary: Django deployment can be easy with Debian packages.
---

# Deployment of Django application as Debian package #

Deployment of a web application is complex.

As I'm a fan of the Debian distribution, I wanted to deploy 1Avis.fr Django
application as a Debian package inside LXC.

## Create the Debian files to build the package ##

If you really don't know what packaging means, I suggest you to read [this
introduction on the Debian
website.](https://wiki.Debian.org/IntroDebianPackaging).

Debian packages are simple archive that are decompressed with couple of scripts
run before/during/after installation.

To make the Django application, you need to create a _debian_ directory. Then
create the control file, changelog etc. as the [Debian
policy](https://www.Debian.org/doc/Debian-policy/) recommends.

Couple of tips for making a Django application as a Debian packages:

- install your code under _/usr/lib/python3/dist-packages_. A Django application
  should be no more, no less of python code ;
- your settings should be under _/etc/_ directory ;
- your conf should be either in the same _/etc/_ directory than your settings or
  directly into the _/etc/_ directory of the software (like
  */etc/nginx/site_available*) ;
- all your media and static files should be under _/var/lib/#PROJECT#_ ;
- binary or command should be system wide available, you can install it under
  the _/usr/bin/_ directory .

Some of the tips come from [this very good
article](https://wiki.debian.org/DjangoPackagingDraft).

Thanks for your attention ;)
