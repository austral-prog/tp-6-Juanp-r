# Replace the "ANSWER HERE" with your answer
def remove_element(list_to_remove_element):
        txt=list_to_remove_element[1:4] + list_to_remove_element[6:]
        return (txt)


def add_elements(lista):
    lista.append('Yellow')
    lista.insert(0,'pink')
    return lista


def is_empty(lista):
    if len(lista) == 0:
        print ("It is empty")
    else:
        print ("It is not empty")


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>3 and len(list_to_compare2)>3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return 0==1


def list_of_lists(list_of_lists_to_modify):
    return [list_of_lists_to_modify[0][0:2],list_of_lists_to_modify[1][1:4],list_of_lists_to_modify[2][-2:]]


  


