def fai2volte(f,a):
    f(a)
    f(a)

def stampa_spam():
    print('spam')

def stamp_arg(str_arg):
    print(str_arg)

def fai_quattro(f,a):
    fai2volte(f,a)
    fai2volte(f,a)

# fai2volte(stampa_spam)
fai2volte(stamp_arg,'ciao')
fai_quattro(stamp_arg,'spam')
