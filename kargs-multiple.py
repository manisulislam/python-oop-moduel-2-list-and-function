def full_name(first, last):
    name= f"full name is : {first} {last}"
    return name

# take parameters in orderly (serial wise)
# res= full_name("anisul", "islam")


# take parameters in on order
name= full_name(last="islam", first="anisul")
print(name)


def famous_name(first, last, **addition):
    name= f"{first} {last}"
    print(addition)
    # single ber korte chile
    print(addition['title'])

    # onek gola ber korte chile
    for key,value in addition.items():
        print(key, value)
    
    return name
name= famous_name(first="anis", last="islam", title="software enginner", addition="programmer")
print(name)


# return multiple
def a_lot(num1, num2):
    sum= num1+num2
    mul= num2*num1
    remain= num2-num1
    # return sum, mul, remain
    return [sum, mul, remain]

everything= a_lot(44, 52)
print(everything)