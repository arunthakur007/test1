obj = [
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :1,"user_name" :"user-1" },
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :2,"user_name" :"user-2" },
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :1,"user_name" :"user-3" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :4,"user_name" :"user-4" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :5,"user_name" :"user-5" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :6,"user_name" :"user-6" },
]


temp = []
emp_data = []
for item in obj:
    data = []
    for  i in obj:
        if i.get("customer_id") == item.get("customer_id"):
            data.append({'user_id': i.get("user_id"), 'user_name': i.get("user_name")})
    # if item.get("customer_id") not in temp:
    #     temp.append(item.get("customer_id"))
        sample = {"customer_details":{
            "customer_id":item.get("customer_id"),
            "customer_name":item.get("customer_name"),
        },
        "user_details":data
        }
        emp_data.append(sample)
print(emp_data)


# my_dict = {'id': '1', 'name': 'customer-1'}
# print(my_dict)
#
# obj = {
# "customer_details" :
#     { "user_id" : 1,
#       "user_name" : "customer-1" },
#     "customer_users":
#         [
#         { "user_id" : 1,
#           "user_name" : "user-1 "},
#         { "user_id": 2,
#           "user_name" : "user-2" },
#         {"user_id": 3,
#              "user_name": "user-3"},
#     ]
# }
# print("Keys : ",obj.keys())
# print(obj.get("customer_details").get("user_id"))
# print(obj.get("customer_details").get("user_name"))
# print("User Id","User Name")
# for i in obj.get("customer_users"):
#     print(i.get("user_id"),i.get("user_name"))




# objd = {"name":"Arun",
#         "name1":"Piyush"
#         }
#
#
# objnew = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30,objd]
# print(objnew[3])
# print(objnew[6])
# print(objnew[8])
# print(objd["name1"])
# print(objd["name"])



# my_dict = {'id': '1', 'name': 'customer-1'}
# print(my_dict)
#
# obj = {
# "customer_details" :
#     { "user_id" : 1,
#       "user_name" : "customer-1" },
#     "customer_users":
#         [
#         { "user_id" : 1,
#           "user_name" : "user-1 "},
#         { "user_id": 2,
#           "user_name" : "user-2" },
#         {"user_id": 3,
#              "user_name": "user-3"},
#     ]
# }
# print("Keys : ",obj.keys())
# print(obj.get("customer_details").get("user_id"))
# print(obj.get("customer_details").get("user_name"))
# print("User Id","User Name")
# for i in obj.get("customer_users"):
#     print(i.get("user_id"),i.get("user_name"))




# objd = {"name":"Arun",
#         "name1":"Piyush"
#         }
#
#
# objnew = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30,objd]
# print(objnew[3])
# print(objnew[6])
# print(objnew[8])
# print(objd["name1"])
# print(objd["name"])



# obj = [
#     {"customer_id" : 1,
#      "customer_name" :"customer-1",
#      "user_id" :1,"user_name" :"user-1" },
#     {"customer_id" : 1,
#      "customer_name" :"customer-1",
#      "user_id" :2,"user_name" :"user-2" },
#     {"customer_id" : 1,
#      "customer_name" :"customer-1",
#      "user_id" :1,"user_name" :"user-3" },
#     {"customer_id" : 2,
#      "customer_name" :"customer-2",
#      "user_id" :4,"user_name" :"user-4" },
#     {"customer_id" : 2,
#      "customer_name" :"customer-2",
#      "user_id" :5,"user_name" :"user-5" },
#     {"customer_id" : 2,
#      "customer_name" :"customer-2",
#      "user_id" :6,"user_name" :"user-6" },
# ]
#
#
# temp = []
# emp_data = []
# for item in obj:
#     data = []
#     for  i in obj:
#         if i.get("customer_id") == item.get("customer_id"):
#             data.append({'user_id': i.get("user_id"), 'user_name': i.get("user_name")})
#     # if item.get("customer_id") not in temp:
#     #     temp.append(item.get("customer_id"))
#         sample = {"customer_details":{
#             "customer_id":item.get("customer_id"),
#             "customer_name":item.get("customer_name"),
#         },
#         "user_details":data
#         }
#         emp_data.append(sample)
# print(emp_data)

# Using list list comprehension
# temp = []
# emp_data = []
# for item in obj:
#     data = [{'user_id': i.get("user_id"), 'user_name': i.get("user_name")}
#             for i in obj if i.get("customer_id") == item.get("customer_id")]
#     if item.get("customer_id") not in temp:
#         temp.append(item.get("customer_id"))
#         emp_data.append({"customer_details":{
#             "customer_id":item.get("customer_id"),
#             "customer_name":item.get("customer_name"),
#         },
#         "user_details":data
#         })
# print(emp_data)

#
# obj = {
# "customer_details" :
#     { "user_id":1,
#       "user_name":"customer-1"},
#
#       "customer_users":
#         [
#         {"user_id":1,
#           "user_name":"user-1"},
#      ],
#     "sdsa":"arun",
# }
#
#
# for i in obj:
#     print(type(i))
#     print(obj[i],"-",type(obj[i]))



# dict1={
#     "name":"arun",
#     "gender":"male",
#     "year":"2022"
# }
# print('dict:\n')
# for i in dict1:
#     print(i,":",dict1.get(i))

obj = [
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :1,"user_name" :"user-1" },
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :2,"user_name" :"user-2" },
    {"customer_id" : 1,
     "customer_name" :"customer-1",
     "user_id" :3,"user_name" :"user-3" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :4,"user_name" :"user-4" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :5,"user_name" :"user-5" },
    {"customer_id" : 2,
     "customer_name" :"customer-2",
     "user_id" :6,"user_name" :"user-6" },
]
print('obj:\n')
for i in obj:
    print(i.get("customer_id"),
          i.get("customer_name"),
          i.get("user_id"),
          i.get("user_name"),
          )