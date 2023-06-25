n = int(input())
counter = 0
for i in range(n):
    num = int(input())
    if num > 1:
	for j in range(2, int(n/2)+1):
		if (n % j) == 0:
			counter = counter
		    break
	    else:
		    counter += 1
    else:
        counter = counter
print(counter)
