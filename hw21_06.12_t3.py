# 3․ Գրել հետևյալ ծրագիրը․
#
#    ------------------------------------------------------------------
#    def decorator_example(func):
#    	...
#
#    @decorator_example
#    def print_avg(x):
#    	return sum(x) / len(x)
#
#    print_avg([4, 5, 9])

def decorator_example(func):
    def inner(*args, **kwargs):
        print('------------------------------------------------------------------')
        print(f'Sum: {sum(*args, **kwargs)}')
        print(f'Length: {len(*args, **kwargs)}')
        print(f'Mean: {func(*args, **kwargs)}')
        print('------------------------------------------------------------------')
    return inner

@decorator_example
def print_avg(x):
    return sum(x) / len(x)

print_avg([4, 5, 9])
