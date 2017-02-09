---
title: What are the globals variables and how to use them ?
date: 2014-03-22
category: programming
tags: global variables, nonlocal, global, aRkadeFR, programming, python3, python
slug: py-global-non-local-variables
author: aRkadeFR
summary: global variable can be very handy, but there's couple of gotcha before using them
---

A good reminder before starting the article is to read the document of the
[global statement](http://docs.python.org/3/reference/simple_stmts.html#the-global-statement),
and the [nonlocal statement](http://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement).

Plus read the part of the language reference on the [naming and
binding](http://docs.python.org/3/reference/executionmodel.html#naming-and-binding),
and then how the [attributes and
methods](http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html)
are called.

We know that we should use the variables in the smaller scope possible, but what
are the globals and nonlocal variables for then? 

Let's see the global interface quickly :

``` python
"""
tests for the global variables
"""
var1 = 1


def fct1():
    global var1
    var1 = 1
    print("this is my global value: {}".format(var1))


def fct2():
    var1 = 2
    print("this is not my global value: {}".format(var1))


if __name__ == "__main__":
    print("""------------------------------
test of the global variables
------------------------------""")
    print("this is my global value: {}".format(var1))
    fct1()
    fct2()
    print("this is my global value: {}".format(var1))

```

	output >
	------------------------------
	test of the global variables
	------------------------------
	this is my global value: 1
	this is my global value: 1
	this is not my global value: 2
	this is my global value: 1
	

As you see, it's neat. Python3 with CPython (and all others if they respect the
standard), access the value of the name variable which is in the closer scope.

If you want to access the global variable, you have to specifically tell python3
with the global statement.

I'm not going into the debat about when and where to use the globals. I will
only advise to you that variable should be in the closer scope.

Now what about the nonlocal variable?

And now it's getting very interesting...


We gonna see all the power of the nonlocal statement with some [closure](http://en.wikipedia.org/wiki/Closure_%28computer_programming%29).

The very basic example is :
	
	def start(x):
		def summarize(y):
			nonlocal x
			return x+y
		return summarize
		
As you can see, we specifically states the x variables is nonlocal and come from
the outer function (start).

This is a good way to help the readability of your programs.

