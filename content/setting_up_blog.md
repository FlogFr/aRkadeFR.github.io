Title: Setting up your pelican blog for free on github
Date: 2013-10-16
Category: sysadmin
Tags: aRkadeFR, sysadmin, pelican, python, blog, hosting, free, github
Slug: setting-up-pelican-blog-free-hosting-github
Author: aRkadeFR
Summary: Setting up your pelican for free on github

You want to setup a blog quickly to share everything with your colleagues and
mates like I'm doing?

You have the solution right in front of you!

I did my blog with pelican, and I host it on github.

Now let's me explain to you how to do it. It's gonna be a very simple tutorial.
Most of it come from [here](http://docs.getpelican.com/en/3.3.0/tips.html).

First of all create git repository on github for your user pages. To do so,
create a repository with this url :

    <user>/<user>.github.io

Clone it in your project directory, and you can start creating your blog now with
pelican.

Which tools do I need ?
- pelican (pip install)
- ghp-import (pip install)
- Markdown (pip install)

To setup a skeleton quickly of a pelican you can execute in a bash this command:

    pelican-quickstart

After answering all the question, you have your skeleton.

Pelican will search in the "content" directory and put the output in the "output"
directory.

Great, let's start! 

So you can write your first post in "content/first_post.md":
    
    Title: First Post
    Date: 2013-10-16 23:10
    Category: sysadmin
    Tags: aRkadeFR
    Slug: first-post-url
    Author: aRkadeFR
    Summary: This is such a beautiful first post

    Change me , please change me !

Now that you have your first post in markdown syntax, pelican will generate your
blog :)

    pelican content -o output -s pelicanconf.py

You can see the output in the "output" directory. You need to feed git to track
these new files :

    git add -- output/\* content/\*

Now let's just give git the output directory in the gh-pages branch. There is
ghp-import for that !
    
    ghp-import output

And to finish, publish it to your git repository.

    git push git@github.com:<user>/<user>.github.io.git gh-pages:master

That's it ? YES ! 

You can see the result of your pelican blog on your url :

    <user>.github.io


Tips:
- to automatized all the process, create a git hooks post-commit with the two
  lasts commands.

