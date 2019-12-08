def giustif_destra(s):
    str_len=len(s)
    print (str_len)
    num_space=70-str_len
    print(num_space)
    giustif_string=(' '*num_space)+(s)
    print (giustif_string)

giustif_destra('fabio')
