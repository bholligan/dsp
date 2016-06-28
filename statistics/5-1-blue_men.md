[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


```python
import brfss, scipy, thinkplot
```
Read data into dataframe
```python
df = brfss.ReadBrfss()
df.columns
```
    Index(['age', 'sex', 'wtyrago', 'finalwt', 'wtkg2', 'htm3'], dtype='object')

Get only the heights of males
```python
heights = df.htm3[df.sex == 1]
```
Initialize cdf for use later
```python
cdf = scipy.stats.norm.cdf
```
Get mean and standard deviation
```python
mean = heights.mean()
sigma = heights.std()
print('Mean: {:.2f}\nStd Dev: {:.2f}'.format(mean, sigma))
```
    Mean: 178.07
    Std Dev: 7.72

Convert heights to centimeters
```python
def convert_height(feet, inches):
    total_inches = feet*12 + inches
    return total_inches*2.54
low_bound = convert_height(5,10)
up_bound = convert_height(6,1)
print('Height range is {:.1f} to {:.1f} cm'.format(low_bound, up_bound))
```

    Height range is 177.8 to 185.4 cm
Find percentage of people between the two height boundaries
```python
percent_pop = (cdf(up_bound, loc = mean, scale = sigma) - cdf(low_bound, loc = mean, scale = sigma))*100
print("{:.2f}%".format(percent_pop))
```

    34.32%

