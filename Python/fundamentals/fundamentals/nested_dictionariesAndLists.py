x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [{
    'x': 10,
    'y': 20
    }]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)

def iterateDictionary(some_list):
    for x in range(0, len(some_list)):
        for key, val in some_list[x].items():
            print(key, " - ", val)

iterateDictionary(students) 

def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list)):
        for key, val in some_list[x].items():
            if key == key_name:
                print(val)
                      
iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)
           
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(str(len(some_dict[key])) + ' ' + key.upper())
        for x in range(0, len(some_dict[key])):
            print(some_dict[key][x])
    
    
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)



