def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'


for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

for i in ['toto', 1, 2, 3]:
    print(i)