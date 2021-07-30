## Cython

#### I got to know that a great way to speed up python codes is to use Cython. Python is very easy to learn and understand, but it is said to be slow. In my experience with using Python, I did not find it to be very slow in practice. That is because there are libraries like numpy and pandas which are C optimized and can easily be integrated and used under the hood of python.

#### Python follows dynamic typing. We do not have to explicitly define the datatypes while declaring variables. The simple way to convert a Python code into Cython is by adding the additional typing information. This proves to significantly speed up the code execution.

#### First, we need to install cython

```
pip install cython

```

#### Then, we need a C/C++ compiler. This installation will vary with the OS you use. I am using Ubuntu, and it comes already installed. 
#### We write a Cython code in a file with .pyx extension
#### In this project, I have a simple for loop implementation in the pure_python.py file and the same implementation in cython_version.pyx file, with the modified type definition ofcourse.

#### Then, we need to build the .pyx file and for that I have the setup.py file. To build the cython file, we will use the command
```
python setup.py build_ext --inplace

```
#### This, will create a build folder (that I have removed), a .c extension file and  a .so extension for cython_version
#### Now, we can simply import cython_version in testing.py and continue testing 
