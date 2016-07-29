# SOLUTION 1
num = 0
while num < 101:
    if num % 5 == 0 and num %3 == 0:
        print "Fizzbuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num

    num = num + 1
#
# # SOLUTION 2
# for num in xrange(1,101):
#     if num % 5 == 0 and num % 3 == 0:
#         print "Fizzbuzz"
#     elif num % 3 == 0:
#         print "Fizz"
#     elif num % 5 == 0:
#         print "Buzz"
#     else:
#         print num
#
# # SOLUTION 3
# for num in xrange(1,101):
#     msg = ""
#     if num % 3 == 0:
#         msg += "Fizz"
#     if num % 5 == 0:
#         msg += "Buzz"
#     if not msg:
#         msg += str(num)
#     print msg
#
# # SOLUTION 4
# for num in xrange(1,101):
#     msg = ""
#     if num % 3 == 0:
#         msg += "Fizz"
#     if num % 5 == 0:
#         msg += "Buzz"
#     print msg or num
