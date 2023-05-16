d = {1 :{'name':'Mohammed',
         'age':21},
      2 :{'name':'Ahmed',
         'age':28}}
 
for key in d:
    if d[key]['age'] >= 22:
        print(d[key]['name'],d[key]['age'] )
 
 