def stringoperation(fn, ln, para, number):
    # Write your code here
    print(fn)
    for i in range(number-2):
        print('\n')
    print(ln)
    print(fn+' '+ln)
    for i in range(number):
        print(fn,end="")
    print('\nThe sentence is {}'.format(para))