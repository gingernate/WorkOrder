repairOrder = {"Tech Name":input("Tech Name: "), "Customer":input("Customer: "), "Unit Number":input("Unit Number: "), "VIN":input("VIN: "), "Make":input("Make: "), "Model":input("Model: "), "Miles":input("Miles: "), "Engine Hours":input("Engine Hours: "), "Complaint":input("Complaint: ")}

while True:
    try:
        vin = input('VIN: ')

        if len(vin) > 17:
            print('VIN must be 17 digits, please retype VIN: ')
        elif len(vin) < 17:
            print('VIN must be 17 digits, please retype VIN: ')
        else:
            break


    except:
        print('VIN must be 17 digits, please retype VIN: ')

for item in repairOrder:
    print("{} = {}".format(item,repairOrder[item]))

