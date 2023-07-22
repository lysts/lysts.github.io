##########################
Introduction to Algorithms
##########################

:date: 2023-07-14 17:24
:tags: algorithms, compsci
:slugs: intro-to-algorithms
:summary: notes on recorded introductory compsci lectures available at MIT OpenCourseWare
:lang: en
:status: published

.. |ex| replace:: example:

.. contents:: Table of Contents
    :depth: 2
    :backlinks: entry

L1: Algorithms & Computation
============================
communicating computational problem solving, its efficiency and correctness


what is a computational problem?
''''''''''''''''''''''''''''''''
computational problems can have multiple correct outputs to an input
—› define a problem by specifying a predicate and observe output (binary)
—› can graph/map out


provide deterministic algorithm to find answer...
'''''''''''''''''''''''''''''''''''''''''''''''''
for general problems, algorithms can accept arbitrarily sized input, doesn't
map what a problem does. "Correctness" defined by whether output is correctly
given.
|
f:I—›O
..
    functional programming definition
|
|ex| birthday problem!::
- maintain record
- check if birthday in record: - if so return pair, - add new student to record, 
- return none


use induction & recursion to prove correctness of algorithm...
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
inductive hypothesis = "if first ''k'' students contain match, algorithm returns
match before interviewing student ''k+1''" = predicate
''k'' increases up to ''n''
base case: ''k=0'' (case holds!)
assume IH true for ''k=k'''{- if k' contains match —› alreated returned by
induction, - else if ''k'+1'' contains match, alg ''k'+1'' against all students}


prove efficiency...
'''''''''''''''''''
dont measure time, instead count fundamental operations (ops), expect performance to depend on (with respect to) size of our input (n) = how well algorithm performs, not how well it's implemented
O(.) upper bound, omega (.) lower bounds (theta) corresponds to both 
asymptotic analysis***


common algorithms that relate algorithm running time to input size: linear time algorithm efficiency from top to bottom:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
::
    (theta)1 = constant time
    ()lg n= logarithmic time
    ()n = linear
    ()n lg n= log n
    ()n^2 = quadratic
    ()n^c = polynomial (c for constant)
    2^(theta)n = exponential time, bad bc if plotted as function of n

—> dnt want shit to go too high. exponential crap!


define model of computation...
''''''''''''''''''''''''''''''
word-RAM (RAM = random access memory, in constant time)
memory (string of bits), CPU where byte (chunk of bits = word) ex 64 bit
machine, to operate on to spit back, addressable memory 20 exabytes!! (data grabbed, registered separately, output also then registered then spat out)
ex can do integer arithmetic, logical ops (boolean etc), bitewise ops, on CPU memory


if you want to operate on non-constant n, linear amount of data, how long will it take?
concerns data structures, store large amount of data and operate on that

