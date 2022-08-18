'''
In this below obj add 
1. dict *
2. list
3. str
4. tuple
'''
obj ={
"dict":{"key":"value"},
"list" :["1","2",2],
"tuple" :(1,2),
"str" :"Arun"
}





# for i in obj:
#     print(i," ------- ",type(obj[i]))

fname_list = [
    "Piyush Kumar",
    "Arun thakur",
    "rohit jamwal"
]

fname_list.remove("rohit jamwal")

for name in fname_list:
    # name = fname_list[2]
    fname = name.split()[0].capitalize()
    lname = name.split()[1].capitalize()

    print("First Name : ",fname)
    print("Last Name : ",lname)



# name="arun thakur"
# print(dir(name))
# # capitalize'title
# print(name.capitalize())

# fname = name.split()[0].capitalize()
# lname = name.split()[1].capitalize()



# print("First Name : ",fname)
# print("Last Name : ",lname)