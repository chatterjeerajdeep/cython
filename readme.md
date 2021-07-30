## Cython

#### I got to know that a great way to speed up python codes is to use Cython. Python is very easy to learn and understand, but it is said to be slow. In my experience with using Python, I did not find it to be very slow in practice. That is because there are libraries like numpy and pandas which are C optimized and can easily be integrated and used under the hood of python.

#### Python follows dynamic typing. We do not have to explicitly define the datatypes while declaring variables. The simple way to convert a Python code into Cython is by adding the additional typing information. This proves to significantly speed up the code execution.

#### First, we need to install cython

```
pip install cython
```

#### Then, we need a C/C++ compiler. This installation will vary with the OS you use. I am using Ubuntu, and it comes already installed. 
#### We write a Cython code in a file with .pyx extension
#### In plain python we can initialise a variable like this

```
a = 5
```

#### In Cython, we will need to mention the datatype like this

```
cdef int a = 5
```

While defining function, instead of using def, we can use either cdef or cpdef

```
cdef func():
...
```
#### In this project, I have a simple for loop implementation in the pure_python.py file and the same implementation in cython_version.pyx file.

#### Then, we need to build the .pyx file and for that I have the setup.py file. To build the cython file, we will use the command
```
python setup.py build_ext --inplace
```
#### This, will create a build folder (that I have removed), a .c extension file and a .so extension file for cython_version.pyx
#### Now, we can simply import cython_version in testing.py and continue testing 
#### Here, I have changed the number of iterations to check the difference between the pure python implementation and the cython implementation

### Results Obtained
>Iteration: 1,Cython worked faster than python by 47.67230796473728 times
>Iteration: 101,Cython worked faster than python by 66.76014944535251 times
>Iteration: 201,Cython worked faster than python by 66.3349647621788 times
>Iteration: 301,Cython worked faster than python by 70.33705667424746 times
>Iteration: 401,Cython worked faster than python by 65.1726105471751 times
>Iteration: 501,Cython worked faster than python by 64.54965532545418 times
>Iteration: 601,Cython worked faster than python by 68.64217024455532 times
>Iteration: 701,Cython worked faster than python by 63.914523996850676 times
>Iteration: 801,Cython worked faster than python by 66.27060800405158 times
>Iteration: 901,Cython worked faster than python by 65.9698829151018 times

#### On an average, for this simple experiment, I found Cython to work almost 65 times faster than the pure python implementation

