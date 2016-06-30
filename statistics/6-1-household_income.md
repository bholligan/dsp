[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)



```python
%matplotlib inline
import hinc2, hinc
import numpy as np
import pandas as pd
import thinkplot, thinkstats2, math
df = hinc.ReadData()
log_sample = hinc2.InterpolateSample(df, log_upper=6.0)
log_cdf = thinkstats2.Cdf(log_sample, label = 'Log CDF')
thinkplot.Cdf(log_cdf)
```

![png](output_4_1.png)

```python
median = log_cdf.Value(.5)
mean = log_sample.mean()
var = log_sample.var()
std = math.sqrt(var)
print('Median = {:.3f}\nMean = {:.3f}'.format(mean, median))
```

    Median = 4.658
    Mean = 4.709


Write functions for central moment and skewness per the textbook. Then calculate Pearson's skew.


```python
def raw_moment(xs, k):
    return sum(x**k for x in xs)/len(xs)
def central_moment(xs, k):
    mean = raw_moment(xs, 1)
    return sum((x-mean)**k for x in xs)/len(xs)
def standardized_moment(xs, k):
    var = central_moment(xs,2)
    std = math.sqrt(var)
    return central_moment(xs,k)/std**k
def skewness(xs):
    return standardized_moment(xs,3)

print("Skewness = {:.4f}".format(skewness(log_sample)))
```

    Skewness = -0.6414



```python
def pearson_skew(xs):
    median = np.median(xs)
    mean = raw_moment(xs,1)
    var = central_moment(xs,2)
    std = math.sqrt(var)
    gp = 3*(mean-median)/std
    return gp

print("Pearson skewness = {:.4f}".format(pearson_skew(log_sample)))
```

    Pearson skewness = -0.3379


There is a left skew on the data. With the Skewness factor being larger than Pearson's.


```python
print("Percent of households below the mean = {:.2f}%".format(
        log_cdf.Prob(mean)*100))
```

    Percent of households below the mean = 45.06%


Let's investigate how the skewness changes if the max salary is 5 million.


```python
new_upper = np.log10(5000000)

log_sample2 = hinc2.InterpolateSample(df, log_upper=new_upper)

print("Skewness = {:.4f}".format(skewness(log_sample2)))
print("Pearson skewness = {:.4f}".format(pearson_skew(log_sample2)))
```

    Skewness = -0.1733
    Pearson skewness = -0.2698


Not surprisingly, adding more data points of higher wealth values brough the skewness back towards the middle. Still a left skew, but it's now less pronounced.

