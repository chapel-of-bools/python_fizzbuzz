# SOLUTION 1
count = 0
while count < 101:
    if count % 5 == 0 and count %3 == 0:
        print "Fizzbuzz"
    elif count % 3 == 0:
        print "Fizz"
    elif count % 5 == 0:
        print "Buzz"
    else:
        print count

    count = count + 1

# SOLUTION 2
for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "Fizzbuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num

# SOLUTION 3
for num in xrange(1,101):
    msg = ""
    if num % 3 == 0:
        msg += "Fizz"
    if num % 5 == 0:
        msg += "Buzz"
    if not msg:
        msg += str(num)
    print msg

# SOLUTION 4
for num in xrange(1,101):
    msg = ""
    if num % 3 == 0:
        msg += "Fizz"
    if num % 5 == 0:
        msg += "Buzz"
    print msg or num
