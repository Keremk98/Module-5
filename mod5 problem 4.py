Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for divisiblebyboth in range(51):
    if divisiblebyboth % 3 == 0 and divisiblebyboth % 5 == 0:
        print("divisible by both")
        continue
    elif divisiblebyboth % 3 == 0:
        print("divisible by three")
        continue
    elif divisiblebyboth % 5 == 0:
        print("divisible by five")
        continue
    print('divisible by both')

    
divisible by both
divisible by both
divisible by both
divisible by three
divisible by both
divisible by five
divisible by three
divisible by both
divisible by both
divisible by three
divisible by five
divisible by both
divisible by three
divisible by both
divisible by both
divisible by both
divisible by both
divisible by both
divisible by three
divisible by both
divisible by five
divisible by three
divisible by both
divisible by both
divisible by three
divisible by five
divisible by both
divisible by three
divisible by both
divisible by both
divisible by both
divisible by both
divisible by both
divisible by three
divisible by both
divisible by five
divisible by three
divisible by both
divisible by both
divisible by three
divisible by five
divisible by both
divisible by three
divisible by both
divisible by both
divisible by both
divisible by both
divisible by both
divisible by three
divisible by both
divisible by five
>>> 