#Function With Arguments and Using of Return 

def avg(a,b,quote):
    sum = a+b
    return f"{sum} {quote}"

sum = avg(quote="kidding",a=3,b=4)
print(sum)
