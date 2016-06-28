[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> I pulled in the baby weight data using Allen Downey's first.py file. The following is a simple calculation of Cohen's D.  
```python
import first
import math
live, firsts, others = first.MakeFrames()
def cohen_d(sample1, sample2):
    numerator = sample1.mean() - sample2.mean()
    n1, n2 = len(sample1), len(sample2)
    s1, s2 = sample1.var(), sample2.var()
    s_squared = (n1*s1 + n2*s2)/(n1+n2)
    cohen = numerator / math.sqrt(s_squared)
    return cohen
print("The Cohen's D for the weight of the first baby compared to the weight of other babies is {0:.4f}"
        .format(cohen_d(firsts.totalwgt_lb, others.totalwgt_lb)))
```

>> The Cohen's d output of this code is -0.0887. This value is small and indicates the weights of first babies and other babies are very similar.
