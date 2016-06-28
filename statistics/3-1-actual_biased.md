[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

The takeaway from this exercise is the pronounced difference between the actual and biased means. The The actual mean is 1 kid per household, while the biased result is almost 2.5 kids.
```python
%matplotlib inline
import chap01soln, thinkstats2, thinkplot
resp = chap01soln.ReadFemResp()
unbiased_pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual')
print("The unbiased mean is {:.4f}".format(unbiased_pmf.Mean()))
```
    The unbiased mean is 1.0242
```python
def bias_pmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    
    for x,p in pmf.Items():
        new_pmf.Mult(x,x)
        
    new_pmf.Normalize()
    return new_pmf
    
biased_pmf = bias_pmf(unbiased_pmf, 'bias')
print("The biased mean is {:.4f}".format(biased_pmf.Mean()))
```
    The biased mean is 2.4037
```python
thinkplot.Pmfs([biased_pmf, unbiased_pmf])
thinkplot.Show(xlabel = "Kids per Household", ylabel = "PMF")
```


![png](output_3_0.png)
