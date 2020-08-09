



def create_spreadsheet(title, row_count=1000):
    print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")


create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)
print("Low limit: " + str(low) + ", high limit: " + str(high))

#Tenth Power
#Write a function named tenth_power() that has one parameter named num.

#The function should return num raised to the 10th power.

# Write your tenth_power function here:
def tenth_power(num):
  return num**10
# Uncomment these function calls to test your tenth_power function:
#print(tenth_power(1))
print(tenth_power(1))
# 1 to the 10th power is 1
#print(tenth_power(0))
print(tenth_power(0))
# 0 to the 10th power is 0
#print(tenth_power(2))
print(tenth_power(2))
# 2 to the 10th power is 1024


print (Jean)













