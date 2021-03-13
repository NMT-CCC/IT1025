# Nicole Terry IT1025
# In D&D, you must roll four 6 sided and disregard the lowest for your stats in character creation. 
# Here, I try to automate that process.

#first, we have to import the ability to randomize numbers.
import random

#Then we have the actual dice rolls

stat1 = [random.randint(1,6) for i in range(4)] #roll four 6 sided die
stat1.remove(min(stat1)) #drop lowest die in the list
stat1total = sum(stat1)

stat2 = [random.randint(1,6) for i in range(4)]
stat2.remove(min(stat2))
stat2total = sum(stat2)

stat3 = [random.randint(1,6) for i in range(4)]
stat3.remove(min(stat3))
stat3total = sum(stat3)

stat4 = [random.randint(1,6) for i in range(4)]
stat4.remove(min(stat4))
stat4total = sum(stat4)

stat5 = [random.randint(1,6) for i in range(4)]
stat5.remove(min(stat5))
stat5total = sum(stat5)

stat6 = [random.randint(1,6) for i in range(4)]
stat6.remove(min(stat6))
stat6total = sum(stat6)

print (stat1total, stat2total, stat3total, stat4total, stat5total, stat6total)
