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