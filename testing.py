import timeit

for i in range(1, 1000, 100):
	cy = timeit.timeit('''cython_version.test(5000)''', setup='import cython_version', number = 1000)
	py = timeit.timeit('''pure_python.test(5000)''', setup = 'import pure_python', number = 1000)

	print("Iteration: {},Cython worked faster than python by {} times".format(i, py/cy))
