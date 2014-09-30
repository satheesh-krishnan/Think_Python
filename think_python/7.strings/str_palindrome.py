def pali(a):
    b=a[::-1]
    if a==b:
         print 'palindrome'
    else:
          print 'not palindrome'
x=raw_input('enter string\n')
y=pali(x)    
