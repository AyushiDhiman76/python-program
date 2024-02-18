#WAP TO COUNT OCCURANCE OF EACH ELEMENTS IN THE LIST.
lst =[4,8,9,5,2,6,4,78,9]
def countx(lst,x):
    count=0
    for i in lst:
        if (i== x):
            count=count+1
    return count
x=8
print('{} has occurred {} times'.format(x,countx(lst,x)))
    

