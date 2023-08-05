def divide_by_zero():
    try:
        result = 5/0
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Result is:", result)
    divide_by_zero()