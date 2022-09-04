# dictionary that will contain all inputs to request a repair order
repair_order = {}

# tech name
name = input('Technician: ')
repair_order['Technician Name:'] = name

# customer info (this will need to also include address, may eventualy )
cust = input ('Customer: ')
repair_order['Customer: '] = cust

# info of vehicle being worked on
unit = input('Unit Number: ')
repair_order['Unit Number: '] = unit
# vin length verification
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
repair_order ['VIN: '] = vin

make = input('Make: ')
repair_order['Make: '] = make

model = input('Model: ')
repair_order['Model: '] = model

miles = input('Vehicle milage: ')
repair_order['Vhicle Milage: '] = miles

hrs = input('Engine Hours: ')
repair_order['Engine Hours: '] = hrs

complaint = input('Customer complaint: ')
repair_order['Customer Complaint: '] = complaint

print (*repair_order.items(), sep='\n')

# ro_upper = dict((k.upper(), v) for k, v in repair_order .items())


