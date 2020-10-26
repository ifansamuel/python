def hitung_kata(str1, str2):
    list_kata = str2.split()
    retval = 0
    for i in list_kata:
        if i == str1:
            retval+=1
    return retval