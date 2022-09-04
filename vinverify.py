# check vin against model database

# will need to add all knowm makes and models to database then import
#
# also will need to autofill model instead of asking for user input in main program


vin = ()
while True:
    try:
        vin = input('enter a vin: ')

        if len (vin) != 17:
            print('VIN must be 17 digits, please re enter vin')
        else:
            break
    except:
        print(vin)

make = vin[2]
print (make)

peterbilt = 'p'
kenworth = 'k'

#this part needs to be fixed.... its too simple. needs to verify possibly 100 diff models
for i in make:
    if make == peterbilt:
        print ('its a peterbilt')
    elif make == kenworth:
        print ('its a kenworth')
    else:
        print ('unknown make')
        break
