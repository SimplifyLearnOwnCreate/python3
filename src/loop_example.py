
from threading import Timer as Timeout

"""
    While loop
    
    Repeat body if condition is true
    
    General format:
    
    while condition:            # if condition is true, execute body
    statement(s)
    else:                       # execute if loop body never executes
    statement(s)
    """

SIZE_OF_HARD_DRIVE_IN_GB = 4
storage_used_in_gb = 4

while storage_used_in_gb < SIZE_OF_HARD_DRIVE_IN_GB:
    remaining_storage = SIZE_OF_HARD_DRIVE_IN_GB - storage_used_in_gb
    print("Remaining storage space: {remaining}".format(remaining=remaining_storage))
    storage_used_in_gb += 1
else:
    print("Hard drive is full.")

def temperature_drop():
    global tea_temperature
    tea_temperature = tea_temperature - 10
    print("Tea's temperature: {temperature}".format(temperature=tea_temperature))

number_of_seconds = 5
tea_temperature_drop_over_time = Timeout(number_of_seconds, temperature_drop)




"""
    While loop
    
    Repeat body if condition is true
    
    General format:
    
    while condition:            # if condition is true, execute body
    statement(s)
    else:                       # execute if loop body never executes
    statement(s)
    """


tea_temperature = 50
print("Tea temperature: {temperature}".format(temperature=tea_temperature))

tea_temperature_drop_over_time.start()

while tea_temperature > 40:
    pass

print("Tea is warm enough to drink.")




# For loop
#
#      Repeat body if condition is true
#
# for item in items:           # Assign an item from items
#     statement(s)
# else:                        # execute if loop never executes
#     statement(s)



transactions = [25, 45, 50, 34]

total = 0

item = 1

for transaction in transactions:
    if transaction == 45:
        continue
    print("Item {item}: {price}".format(item=item, price=transaction))
    total += transaction
    item += 1
    if total > 60:
        print("You have exceed your weekly budget.")
        break

print("Total: {total}".format(total=total))
