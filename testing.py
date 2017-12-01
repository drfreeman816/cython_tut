import timeit

n_tests = 10000000

cy = timeit.timeit('example_cy.test(5)',
                   setup='import example_cy', number=n_tests)

print('Cython', cy)


py = timeit.timeit('example_py.test(5)',
                   setup='import example_py', number=n_tests)

print('Python', py)

print('Cython is {}x faster'.format(py / cy))
