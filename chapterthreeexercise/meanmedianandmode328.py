"""
 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median and
 mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. Suppose the values included an
other 34. What problem might occur? 
"""

import statistics

values = [9, 11, 22, 34, 17, 22, 34, 22, 40,34]

mean = statistics.mean(values)


median = statistics.median(values)


mode = statistics.mode(values)


print("mean", mean)
print("median", median)
print("mode", mode)