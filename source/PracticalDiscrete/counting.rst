..  Copyright (C) Mark Betnel
    Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation. A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Counting
..  description:: This is a chapter about funny ways of counting things

.. _counting_stuff:

How many are there?
===================

How many different ways are there to...


.. index:: combinations, permutations, factorial, loops, sets, proof, logic, induction, contradiction, counterexample, evidence

TEXT

.. activecode:: ch04_1

    import turtle

    def drawSquare(t, sz):
        """Make turtle t draw a square of with side sz."""

        for i in range(4):
            t.forward(sz)
            t.left(90)


    wn = turtle.Screen()              # Set up the window and its attributes
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()            # create alex
    drawSquare(alex, 50)             # Call the function to draw the square

    wn.exitonclick()


Glossary
--------

.. glossary::

    permutation
	A permutation of a set is a way of rewriting the members of the 
	set in a different order.  How many different permutations of a
	set are possible is one of our fundamental questions.

    combination
	A combination of a set is  TODO

