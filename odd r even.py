def is_even():
    x = int(raw_input("Enter number"))
    if x % 2 == 0:
        return x, "is an even number"
    else:
        return x, "is an odd number"
print is_even()
