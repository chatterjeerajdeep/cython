# Cython Projects

## Project 1 - Use of simple for loop
 In this project, I tried the simple example of implementing a for loop in Cython. I learned that perhaps the simplest way to make a cython version of the python implementation, is to explicitly define the data types of every variable being used and functions that are being defined. 

 I checked the time of execution of the for loops for the python and the cython versions with varying number of iterations. 

 I observed a speed up of about **65 times** in the cython version over the python version on an average.

## Project 2 - Implementing Conway's game of life in Python and Cython and visually representing the speed up effect
In this project, I tried to implement the famous Conway's Game of Life in python and in cython. This is a very interesting work because I am able to plot the generation of new states in a matplolib figure and refresh it at the rate by which the new figures are being generated.

The cython version, as expected, generates the new states much faster than the python version and hence the image gets refreshed at a faster rate for the cython implementation. I captured this difference in the form of a video and was able to visually appreciate the speed up in Cython!