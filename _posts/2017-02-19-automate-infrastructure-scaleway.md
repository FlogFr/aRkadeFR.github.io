---
layout: default
title: Automate your cloud infrastructure with Scaleway API
description: Automate your cloud infrastructure with Scaleway API
date: 2017-02-19
categories: [system]
---

# Automate your cloud infrastructure with Scaleway CLI

## Install and configure your API token

Go to https://cloud.scaleway.com/#/credentials and configure your credentials.
You need to remember your Organization uuid and Token uuid.

The API is then available from `cp-#region#.scaleway.com`, and all data is sent
and received as JSON.

A curl example:
```
$ curl -H "X-Auth-Token: ${SCW_TOKEN}" -H "Content-Type: application/json"
https://cp-par1.scaleway.com/volumes/ -i
```


## Create, test, and destroy a resource

We now want to automatically create, test, and destroy a new Scaleway instance.

```
$ export SCW_TOKEN="#TOKEN#"
$ export SCW_ORGANIZATION="#ORGANIZATION#"
$ curl -H "X-Auth-Token: ${SCW_TOKEN}" -H "Content-Type: application/json"
https://cp-par1.scaleway.com/servers/ -i
$ curl -H "X-Auth-Token: ${SCW_TOKEN}" -H "Content-Type: application/json"
-X POST -d "{…}" https://cp-par1.scaleway.com/servers/
```


## References

- [Scaleway API documentation](https://developer.scaleway.com/)
- [Scaleway Account Credentials](https://cloud.scaleway.com/#/credentials)
