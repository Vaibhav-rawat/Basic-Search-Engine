'''This program is used to demonstrate the logic behind how we can search for a word in any string and print out the number of result
from High to low.
Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
def compare(sens,sens1):
    a=sens.split(' ')
    b=sens1.split(' ')
    count=0
    for i in a:
        for j in b:
            if j.lower()==i.lower():
                count+=1
    return count

   
list_=['python is good','vaibhav knows vaid','vaibhav is learning python']
q_word=input('Enter the string you want to search\n')
search=[compare(l,q_word) for l in list_]
sorted_search=[i for i in sorted(zip(search,list_),reverse=True) if i[0]!=0]
print(f'Total result found => {len(sorted_search)}')
for a,b in sorted_search:
    print(f'result found {a} in \"{b}\"')
