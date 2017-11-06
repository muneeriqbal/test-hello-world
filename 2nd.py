def donuts(counts):


     if counts>10:
        a= "dounts are many"

     else:
            a="donuts are = "+str(counts)


     return\
           print(a)




def both_ends(s):

    if (len(s)>2):
        text = s
        a = text[0:2]
        b = text[-2:]
        c = text[:6]
        d = text[6:]
        e = text[2:6]
        result = a+b
    else:
        result= "empty string"
        return \
            print(result)



def fix_start(st):

    s=st[0]
    b=st[1:].replace(s,"*")
    return print(s+b)


def mix_up(a, b):
    a1 = a[:2]

    b1 = b[:2]

    c = a[2:].replace(b1,"")

    d = b[2:].replace(a1,"")

    return (b1+c, a1+d)



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print
    '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print
    'donuts'
     #Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')
    test(donuts(109), 'Number of donuts: many')

    print
    print
    'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print
    print
    'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')


    print
    print
    'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    test(mix_up('muneer', 'iqbal'), 'iqneer mubal')


 #Standard boilerplate to call the main() function.
if __name__ == '__main__':
   main()
