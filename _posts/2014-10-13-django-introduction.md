---
resource: true
title: Handling generic exceptions
description: django-exceptions is a Pip package to use for handling exceptions to not throw a 500 error to the client by redirecting or rendering a template.
date: 2014-10-13
categories: [development]
---

# When should I use django-exceptions ?

In my case, I got a whole big project into my hands, and some internal error
appears a bit from everywhere, throwing 500 to the client, and to all my
monitoring tools.

This can be very helpful except when the 500 error isn't a real one…

For instance, the main project works with some third API. If the request fails,
I'm throwing an APIException. But this shouldn't throw a 500 to the client. The
error doesn't come from this app, but from the remote API.

# How to use it ?

With the very same example, I wanted to render a template with a little message:
'The remote API is currently experiencing some trouble, please try again later'.
So you pip install django-excetions, then extends your APIExceptions from:
django\_exceptions.exceptions.RedirectException.
You provide either a template\_name or a redirect\_view to the class, and that's
it. You're ready to go.

Ah! One last thing, same as usual: installation is pip install django-exceptions
plus adding the middleware django\_exceptions.middleware.ExceptionsMiddleware.

Thank for reading :)
