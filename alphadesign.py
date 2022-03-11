def print_rangoli(size):
     lst='abcdefghijklmnopqrstuvwxyz' 
     size2=size
     num=2*size -1
     for d in range(0,num):
         if d<=num//2:
             x=((size-1)-d)*2
         else:
             d1=(num-1)-d
             x1=d-(size-1)
             x=(x1)*2
             d=d1
         print('-'*x,end='')
         size=size2
         for i in range(0,2*d):
             if i<=(d):
                  print(lst[size-1]+'-',end='')
                  size=size-1
             else:
                 print(lst[size+1]+'-',end='')
                 size=size+1
         size=size2
         print(lst[size-1],end='')
         print('-'*x)
s=int(input('Enter size: '))
print_rangoli(s)
        