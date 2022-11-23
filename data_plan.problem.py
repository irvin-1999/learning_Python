'''
Rori has a data plan with his cell phone provider that offers him x megabytes of data per month
Any data he doesn't use in a given month carries over to the next month

We're given number of megabytes of data that Rori uses in each of the 1st n months.Our task is to
determine the number of megabytes available for the following  month

Input consist of the following:
@A line containing integer x, the number of mrgabytes given to Rori per month. x is between 1&100
@A line containing integer n, the numberof month that Rori has had the data plan.n is between 1&100
@n lines, one for each month,giving the integer number of megabytes that Rori uses in that month
Each number is atleast 0 and will never outstrip the number of available megabytes
'''

monthly_mb=int(input('Enter monthly mb: \n'))
n=int(input())

total_mb=monthly_mb * (n+1)

for i in range(n):
    used=int(input())
    total_mb=total_mb + monthly_mb - used

print(total_mb)