import timeit

cy = timeit.timeit('''cython_version.test(5000)''', setup='import cython_version', number = 100)
py = timeit.timeit('''pure_python.test(5000)''', setup = 'import pure_python', number = 100)

print("Cython worked faster than python by {} times".format(py/cy))
