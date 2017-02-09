---
title: Language operator precendence aren't the same, gotcha!
date: 2014-03-01
category: programming
tags: aRkadeFR, programming, perl, python, operator, precedence
slug: language-operator-precendence-not-the-same
author: aRkadeFR
summary: Changing of language can be painful, especially for the operator precedence.
---

The difference between the operator precedence among the languages
are huge. Even if you think of it as a minor problem, it will blow up 
in your face every once in a while.

I switch between Perl and Python very often, and I find myself
comfortable with both.

But I got tricked by Perl and its operator precedence. Let's look
at the facts:

    perl> my $test = 0 or 1; print "test = ".$test."\n";
    test = 0

    perl> my $test = (0 or 1); print "test = ".$test."\n";
    test = 1

Now look at the differences with python:
    
    In [1]: test = 0 or 1; print("test = %i" % test)
    test = 1

    In [1]: test = (0 or 1); print("test = %i" % test)
    test = 1

Apart from the fact that it's not very intuitive the operator
precedence in Perl, you should definitely double check the
operator precedence of the language you're programming on.
