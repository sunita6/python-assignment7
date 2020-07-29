#find intersection of nested list

list1=[(1,2),(3,4),(5,6)]
list2=[(3,4),(5,7),(1,2)]
print("original list1:"+str(list1))
print("original list2:"+str(list2))
res_list=[]
for i in list1:
    if i in list2:
        res_list.append(i)
        print("intersection of two list is:"+str(res_list))
        
        
#output
'''
original list1:[(1, 2), (3, 4), (5, 6)]
original list2:[(3, 4), (5, 7), (1, 2)]
intersection of two list is:[(1, 2)]
intersection of two list is:[(1, 2), (3, 4)]
​'''
