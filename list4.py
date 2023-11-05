numbers = []
while True:
    try:
        list = input ("Enter the integer or 'done' to terminate the program: ")
        if list == 'done':
            break
        number = int(list)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print("The average value:",average)
    except:
        print("mistake,please try again")
        
if numbers:
    average = sum(numbers) / len(numbers)
    print("The average value is:",average)
else:
    print("mistake,please try again")                