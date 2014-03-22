Title: What are the globals variables and how to use them ?
Date: 2014-03-22
Category: programming, python
Tags: global variables, nonlocal, global, aRkadeFR, programming, python3, python
Slug: py-global-non-local-variables
Author: aRkadeFR
Summary: global variable can be very handy, but there's couple of gotcha before using them


A good reminder before starting the article is to read the document of the
[global statement](http://docs.python.org/3/reference/simple_stmts.html#the-global-statement),
and the [nonlocal statement](http://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement).

Plus read the part of the language reference on the [naming and
binding](http://docs.python.org/3/reference/executionmodel.html#naming-and-binding),
and then how the [attributes and
methods](http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html)
are called.

We know that we should use the variables in the smaller scope possible, but what
are the globals variables for then? 

Let's play with it quickly:

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


	"""
	tests for the nonlocal keyword
	"""
	def fct3():
		var2 = 2
		def fct31():
			var2 = 4
			print("this is my local value: {}".format(var2))
		fct31()
		print("this is my local value: {}".format(var2))
			
		

	def fct4():
		var2 = 2
		def fct41():
			nonlocal var2
			var2 = 4
			print("this is my local value: {}".format(var2))
		fct41()
		print("this is my local value: {}".format(var2))
		


	if __name__ == "__main__":
		print("""------------------------------
	test of the global variables
	------------------------------""")
		print("this is my global value: {}".format(var1))
		fct1()
		fct2()
		print("this is my global value: {}".format(var1))
		print("""------------------------------
	test of the nonlocal variables
	------------------------------""")
		fct3()
		fct4()


	output >
	------------------------------
	test of the global variables
	------------------------------
	this is my global value: 1
	this is my global value: 1
	this is not my global value: 2
	this is my global value: 1
	------------------------------
	test of the nonlocal variables
	------------------------------
	this is my local value: 4
	this is my local value: 2
	this is my local value: 4
	this is my local value: 4
	

As you see, it's pretty neat.

Now, the whole debat on where and when to use them, and where/when not to.

If you write some pythonic code, your global variables will be very well named,
and your variables won't collide. But it's not a good way of thinking.

As in python3, you need to be very explicit when using a global variable, and
that's a perfect way to warn the programmer before using them.

