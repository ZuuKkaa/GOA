num = 5

#and (და) წერს trues (მართალია) იმ შემთხვევაში თუ ორივე მხარეს შედარება სწორია და ტოლია თუნდაც ერთი შეცდომა იყოს ნებისმიერ მხარეს მაინც false (მცდარია)ს დაწერს. და-ზe

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False 

#or (ან)  წერს trues იმ შემთხვევაში თუ ერთი მაინც სწორია ან მარცენა მხარეს ან მარჯვენა მხარეს თუნდაც შეცდომა იყოს ერთ მაინც trues დაწერს და თუ ორივე შეცდომითაა მაშინ false ს დაწერს. ან-ზე
# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True
print(num >= 1 and num <= 4) # False
print(num > 5 and num <= 10) # False
print(num > 5 and num > 10) # False

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True
print(num >= 1 or num <= 4) # True
print(num > 5 or num <= 10) # True
print(num > 5 or num > 10) # False