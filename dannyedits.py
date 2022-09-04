repairOrder = {"Tech Name":input("Tech Name: "), "Customer":input("Customer: "), "Unit Number":input("Unit Number: ")}

while True:
    try:
        repairOrder = {"VIN":input("VIN: ")}
        if len(repairOrder) == 17:
            break

            print('VIN must be 17 digits, please retype VIN: ')
        elif len(repairOrder) != 17:
            print('VIN must be 17 digits, please retype VIN: ')
        else:
            break


    except:
        print('VIN must be 17 digits, please retype VIN: ')

# while True:
#     try:
#         if len("VIN") > 17 :
#             print("VIN must be 17 digits, please retype VIN")
#         elif len("VIN") < 17 :
#             print("VIN must be 17 digits, please retype VIN")
#         else :
#             break
#     except:
#         break

repairOrder = {"Make":input("Make: "), "Model":input("Model: "), "Miles":input("Miles: "), "Engine Hours":input("Engine Hours: "), "Complaint":input("Complaint: ")}


for item in repairOrder:
    print("{} = {}".format(item,repairOrder[item]))


#     # except ValueError:
#     #     print('VIN must be 17 digits, please enter VIN: ')
#     # continue
# if len(vin) == 17:
#     print ('VIN must be 17 digits, please enter VIN: ')
# else:
#     break