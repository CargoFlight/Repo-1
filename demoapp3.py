'''
numlist= [4,32,6,76,12,37,52]
square = [sol ** 2 for sol in numlist]
print(square)

car = ['tata', 'honda', 'toyota', 'hyundai', 'skoda', 'suzuki', 'mahindra', 'BMW', 'Mercedes']  
# making a new list with condition  
new_carlist = [x for x in car if 'a' in x]        
# printing new list  
print(new_carlist)

name = "Monopoly it Tech for u it "

vowels = "aeiou"

solution = [letter for letter in name if letter in vowels]  

print(solution)  

'''
num = [x for x in range(20)]
print(num)  
