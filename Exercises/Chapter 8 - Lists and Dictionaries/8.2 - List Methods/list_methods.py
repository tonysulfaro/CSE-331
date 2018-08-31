temps = [65, 67, 72, 75]
temps.append(77)
print(temps[-1]) 
#prints 77

actors = ['Pitt', 'Damon']
actors.insert(1, 'Affleck')
print(actors[0], actors[1], actors[2])
#prints Pitt Affleck Damon

#simplest way to sort list then remove largest element
my_list = [1,2,3,15]
my_list.sort() 
my_list.pop()

#statement to count number of 15's
my_list.count(15)