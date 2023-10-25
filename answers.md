# CMPS 2200 Reciation 5
## Answers

**Name:** Jack Zemke


Place all written answers from `recitation-05.md` here for easier grading.







 **1b.**
  -

I utilized the non-recursive version of `ssort` for this comparison. For my fixed pivot, I placed it at `list[len(list)//2]`, or the center of the list. This may explain it's acceptable performance on presorted lists as opposed to selecting `list[0]`. My system was exceeding maximum recursion depth with `list[0]` as the fixed pivot.

Random Permutations:
|     n (shuffled) |     ssort |   qsort-fixed-pivot |   qsort-random-pivot |
|-------|-----------|---------------------|----------------------|
| 100 |   0.104 |               0.437 |                0.094 |
| 150 |   0.219 |               1.063 |                0.139 |
| 200 |   0.361 |               1.868 |                0.192 |
| 250 |   0.557 |               2.908 |                0.249 |
| 300 |   0.774 |               3.991 |                0.331 |
| 350 |   1.056 |               5.253 |                0.358 |
| 400 |   1.382 |               6.696 |                0.428 |
| 450 |   1.718 |               8.250 |                0.470 |
| 500 |   2.117 |              10.042 |                0.563 |
| 750 |   4.665 |              20.966 |                0.853 |




![image](Figure_1.png "Fig 1")

Unshuffled Permutations:
|     n (presorted) |    ssort |   qsort-fixed-pivot |   qsort-random-pivot |
|-------|----------|---------------------|----------------------|
| 100 |   0.086 |               0.444 |                0.088 |
| 150 |   0.176 |               1.053 |                0.143 |
| 200 |   0.299 |               1.845 |                0.207 |
| 250 |   0.458 |               2.864 |                0.254 |
| 300 |   0.653 |               3.988 |                0.304 |
| 350 |   0.876 |               5.217 |                0.363 |
| 400 |   1.130 |               6.634 |                0.408 |
| 450 |   1.423 |               8.195 |                0.477 |
| 500 |   1.749 |               9.987 |                0.606 |
| 750 |   3.861 |              20.797 |                0.832 |


![image](Figure_2.png "Fig 2")

The asymptotic bounds of these sorting methods are as follows:

`ssort`: $\text{Average case time} = O(n^2)$ $\text{Worst case time} = O(n^2)$ 

`qsort-fixed-pivot`: $\text{Average case time} = O(n \log n)$ $\text{Worst case time} = O(n^2)$

`qsort-random-pivot`: $\text{Average case time} = O(n \log n)$ $\text{Worst case time} = O(n^2)$

The running times roughly line up with the asymptotic upper bounds. The `qsort` with random pivot is much closer to `qsort`'s $\text{Average case time} : O(n \log n)$. Meanwhile, the qsort with fixed pivot of `n[0]` is much closer to the $\text{Worst case time} : O(n^2)$. In all trials, `qsort-fixed` was the slowest of all the algorithms. In the presorted lists, chosing `n[0]` is the worst possible pivot choice, leading it to perform in its $\text{Worst case time} : O(n^2)$. ssort performed surprisingly well. Its time complexity increased exponentially in the shuffled trials and slightly slower than exponentially in the presorted trials. 

Neither of the `qsort` implimentations were significantly faster on the shuffled vs presorted input lists. This can be explained by noting that `qsort` performs essentially the same amount of work whether the list is sorted or unsorted, as long as the pivot selection strategy remains the same. `ssort` performed much better on the presorted input lists than the shuffled input lists. This is due to the fact that although the same amount of comparisons were made, there were much more swaps on the shuffled list, which can become costly in high numbers. 





 **1c.**
  -

Shuffled:
|     n (shuffled)  |   timsort |   qsort-random-pivot |
|-------|-----------|---------------------|
| 100 |     0.005 |               0.134 |
| 150 |     0.009 |               0.205 |
| 200 |     0.013 |               0.305 |
| 250 |     0.016 |               0.355 |
| 300 |     0.020 |               0.467 |
| 350 |     0.024 |               0.501 |
| 400 |     0.028 |               0.555 |
| 450 |     0.032 |               0.695 |
| 500 |     0.036 |               0.728 |
| 750 |     0.053 |               1.133 |


![image](Figure_3.png "Fig 3")

Unshuffled:
|     n (presorted) |   timsort |   qsort-random-pivot |
|-------|-----------|---------------------|
| 100 | 0.002 |0.087 |
| 150 | 0.001 |0.140 |
| 200 | 0.001 |0.192 |
| 250 | 0.001 |0.261 |
| 300 | 0.002 |0.328 |
| 350 | 0.001 |0.399 |
| 400 | 0.002 |0.420 |
| 450 | 0.002 |0.488 |
| 500 | 0.002 |0.583 |
| 750 | 0.003 |0.846 |


![image](Figure_4.png "Fig 4")

