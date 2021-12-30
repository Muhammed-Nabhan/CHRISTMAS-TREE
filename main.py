height=16
wood=height//3
floor=1
k=1
print('###===***THE CHRISTMAS TREE***===###') 
for i in range(height):
    print((' ' * (height - i)) + ( '*' * ((2 * i) + 1)))
    
for i in range(wood):
     print(('  '*((height-1)//2))+('#' * wood) )
for i in range(floor):
    for j in range(k):
       print('v '*18)
       print('@@'*18)
       print('o0'*18)
    

