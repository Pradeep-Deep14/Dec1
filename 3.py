def join_strings(s1,s2):
    str1= s1 + " " + s2
    str2= " ".join([s1,s2])
    return str1 == str2

str_1 = "hello"
str_2 = "world"

print(join_strings(str_1,str_2))
