name = ()
name = input('Name: ').upper()
name = ('Tech Name: ') + name

customer = ()
customer = input('Customer: ').upper()
customer = ('Customer: ') + customer

unit = ()
unit = input('Unit Number: ').upper()
unit = ('Unit Number: ') + unit

vin = ()
while True:
    try:
        vin = input('VIN: ').upper()

        if len(vin) > 17:
            print('VIN must be 17 digits, please retype VIN: ')
        elif len(vin) < 17:
            print('VIN must be 17 digits, please retype VIN: ')
        else:
            break


    except:
        print('VIN must be 17 digits, please retype VIN: ')
vin = ('VIN: ') + vin

make = ()
make = input('Make: ').upper()
make = ('Make: ') + make

model = ()
model = input('Model: ').upper()
model = ('Model: ') + model

miles = ()
miles = input('Miles: ').upper()
miles = ('Vehicle Milage: ') + miles

hrs = ()
hrs = input('Engine Hours: ').upper()
hrs = ('Engine Hours: ') + hrs

complaint = ()
complaint = input('Customer Complaint: ').upper()
complaint = ('Customer complaint: ') + complaint

repairOrder = name, customer, unit, vin, make, model, miles, hrs, complaint

# print (repairOrder)
print (*repairOrder,sep='\n' )