

str = 'ajsjsajjfafjasdfjkasd'

list_str = list(str)
no_repeat = ''

lista = []
j=0
i=0
for i in range(len(str)):
    for j in range(len(str)):
        shkr = str[i:j]
        no_repeat = no_repeat + shkr
        if shkr in no_repeat:
            break
        else:
            i + 1
            j = i
            break
        break
        #fjale = fjale + shkr

    lista.append(no_repeat)

print(lista)






print(lista)





