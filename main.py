import random, time
import tabulate


def qsort(a, pivot_fn):
    # print(a)
    if len(a) == 0 or len(a) == 1:
        return a
    p = pivot_fn(a)
    # print(p)
    l = list(filter(lambda x: x<p, a))
    r = list(filter(lambda x: x>p, a))
    sl = qsort(l,pivot_fn)
    sr = qsort(r,pivot_fn)
    return sl + [p] + sr

# print(qsort((list(range(100))), random.choice))
# print(qsort([3,8,7,1,4,9,10,42], lambda x: x[0]))
# a = (list(range(1000)))
# random.shuffle(a)
# print(a)
# print(qsort(a,random.choice))
# print(random.shuffle(list(range(1,100))))

def ssort(L):
    for i in range(len(L)):
        # print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 150, 200, 250, 300, 350, 400, 450, 500, 750]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    def qsort_fixed_pivot(a):
        return qsort(a, lambda x: x[0])
    def qsort_random_pivot(a):
        return qsort(a, random.choice)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        random.shuffle(mylist)
        # print(mylist)
        # print(mylist)
        result.append([
            len(mylist),
            time_search(tim_sort, mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    a = tabulate.tabulate(results,
                            headers=['n', 'timsort', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github")
    print(a)
    return a

results = compare_sort()
def test_print():
    print_results(compare_sort())

random.seed()
test_print()

# # plot raw timing data and best fit curves.

# import matplotlib.pyplot as plt
# # %matplotlib inline
# import math
# from scipy.optimize import curve_fit
# import numpy as np

# sizes = [x[0] for x in results]
# linear_times = [x[3] for x in results]
# binary_times = [x[2] for x in results]
# qsort_random = [x[3] for x in results]
# fig, ax = plt.subplots(1)
# ax2 = ax.twinx()
# ax2.plot(
#          sizes,
#          linear_times,
#          'bo-'
#        )
# ax2.set_ylabel('ssort', color='blue', size=20)
# ax2.tick_params(axis='y', labelcolor='blue')
# ax.plot(
#          sizes,
#          binary_times,
#          'ro-'
#         )
# ax.set_ylabel('qsort-fixed', color='red', size=20)
# ax.tick_params(axis='y', labelcolor='red')
# ax.set_xlabel('n', size=20)

# def lgn(i, beta, beta0):
#     # beta*lg(n) + beta0
#     return beta*np.array([math.log(x, 2) for x in i] ) + beta0

# def linearn(i, beta, beta0):
#     # beta*n + beta0
#     return beta*np.array(i) + beta0

# lgn_beta, _ = curve_fit(lgn, sizes, binary_times)
# ax.plot(sizes, lgn(sizes, *lgn_beta), 'r--', label='lg fit (beta=%.2g, beta0=%.2g)' % (lgn_beta[0], lgn_beta[1]))
# ax.legend(loc='upper left')

# linearn_beta, _ = curve_fit(linearn, sizes, linear_times)
# ax2.plot(sizes, linearn(sizes, *linearn_beta), 'b--', label='linear fit (beta=%.2g, beta0=%.2g)' % (linearn_beta[0], linearn_beta[1]))
# ax2.legend(loc='lower right')
# plt.show()

import matplotlib.pyplot as plt

def graph():
    sizes = [x[0] for x in results]
    ssort = [x[1] for x in results]
    qsort_fixed = [x[2] for x in results]
    qsort_random = [x[3] for x in results]
    # print(l)
    # print(n)
    # print(t)
    plt.plot(sizes,ssort, label = 'timsort')
    # plt.plot(sizes,qsort_fixed, label = 'qsort_fixed')
    plt.plot(sizes,qsort_random, label = 'qsort_random')
    plt.legend()
    plt.title('timsort vs qsort_random')
    plt.xlabel('size of input list, shuffled')
    plt.ylabel('Time required to execute')
    plt.yscale('symlog')
    plt.xscale('log')
    plt.show()

graph()