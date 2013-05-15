..  Copyright (C) Mark Betnel
    Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation. A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Graphs
..  description:: This is a chapter about Graphs

.. _graph_theory:

How do you get there from here?
===============================

Suppose you wanted to plan a trip through the city, stopping at some interesting sites along the way.  You don't really care what order you visit them in, so long as you visit all of them, and as long as you minimize how much time you have to spend walking -- you're a little lazy, and really, you just want to see stuff.  How do you go about planning your walk?


.. index:: graph, tour, path, cycle, Euler

TEXT


Glossary
--------

.. glossary::

    graph
	A graph is a collection of nodes and edges that connect those nodes.

    node
	Another name for point, location, person, site -- any*thing* that you
	represent on a graph as a place to go to is a *node*.

    edge
	Another name for line, bridge, connection.  The edges in a graph
	define how to get from one *node* to another.  In some graphs
	the edges are directional, as in you can only cross them in one
	direction. In most graphs they are bi-directional, meaning there is
	no difference between the two ways you might cross them.

    weight
	In some graphs, the edges have *weights*, which indicate the cost
	of using that particular connection.  If the graph nodes represent
	cities, then the edges would indicate roads between the cities, and
	the weights would represent the distance between them.



	"The sun is yellow AND the sun is NOT yellow" is a contradiction.  
	If we are speaking logically, both of those claims cannot be true
	at the same time -- they *contradict* each other.	



