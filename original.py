# this file is just a mess, mostly unusable code. saving for reference

# dictionary or list that will contain all information required for repair order
# ro = ['Tech Name: ', 'Customer: ', 'Unit Number: ', 'VIN: ', 'Make: ', 'Model: ', 'Miles: ', 'Engine Hours: ', 'Complaint: ']

repairOrder = {"Tech Name":input("Tech Name: "), "Customer":input("Customer: "), "Unit Number":input("Unit Number: "), "VIN":input("VIN: "), "Make":input("Make: "), "Model":input("Model: "), "Miles":input("Miles: "), "Engine Hours":input("Engine Hours: "), "Complaint":input("Complaint: ")}
print (repairOrder)
# name = input('Name: ')
# repairOrder.insert(1, name)
# customer = input('Customer: ')
# repairOrder.insert(3, customer)
# unit = input('Unit Number: ')
# repairOrder.insert(5, unit)

# while True:
#     try:
#         vin = input('VIN: ')

#         if len(vin) > 17:
#             print('VIN must be 17 digits, please retype VIN: ')
#         elif len(vin) < 17:
#             print('VIN must be 17 digits, please retype VIN: ')
#         else:
#             break


#     except:
#         print('VIN must be 17 digits, please retype VIN: ')
# #     # except ValueError:
# #     #     print('VIN must be 17 digits, please enter VIN: ')
# #     # continue
# # if len(vin) == 17:
# #     print ('VIN must be 17 digits, please enter VIN: ')
# # else:
# #     break

# repairOrder.insert(7, vin)
# make = input('Make: ')
# repairOrder.insert(9, make)
# model = input('Model: ')
# repairOrder.insert(11, model)
# miles = input('Miles: ')
# repairOrder.insert(13, miles)
# hrs = input('Engine Hours: ')
# repairOrder.insert(15, hrs)
# complaint = input('Customer Complaint: ')
# repairOrder.insert(17, complaint)

# for i in range(len(repairOrder)):
#     repairOrder[i] = repairOrder[i].upper()

# print (*repairOrder,sep='\n' )
