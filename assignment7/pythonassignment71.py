#code to demonstrate to swap key and value

old_dict={21:"FTP",22:"SSH",23:"telnet",80:"http"}
new_dict=dict([(v,k) for k,v in old_dict.items()])
print("original dictionary is")
print(old_dict)
print()
print("dictionary after swapping is:")
print("keys:values")
for i in new_dict:
    print(i,":",new_dict[i])

'''
output:
original dictionary is
{21: 'FTP', 22: 'SSH', 23: 'telnet', 80: 'http'}

dictionary after swapping is:
keys:values
FTP : 21
SSH : 22
telnet : 23
http : 80
'''




