# <--- Recursive program to print even numbers b/w 2 limit --->
def print_even(limit1, limit2):
    if limit2 < limit1:
        return limit2
    else:
        if limit1 % 2 == 0:
            print(limit1, end="  ")
        print_even(limit1 + 1, limit2)


print_even(10,20)