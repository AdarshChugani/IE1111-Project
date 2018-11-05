import pandas as pd
import numpy as nm
Students = {}
Working_Adults = {}
Elderly = {}
Equivalence = {'Seldom (< 1 time a week)' : 0.5,
'1 - 2 times a week' : 1.5,
'3 - 4 times a week' : 3.5,
'5 - 6 times a week' : 5.5,
'7 times a week' : 7}
df = pd.read_csv('IE1111 Kaya Data.csv')
df = df[df['S/N'].notnull()]
df.columns = df.columns.str.strip()
for i in range(120):
    if (df['What is the age demographic of the customer?'][i]) == 'Student':
        if(df['Per Week, how often do you eat Kaya Toast?'][i]) not in Students:
            Students[df['Per Week, how often do you eat Kaya Toast?'][i]] = 1
        else:
            Students[df['Per Week, how often do you eat Kaya Toast?'][i]] += 1
            
    elif (df['What is the age demographic of the customer?'][i]) == 'Working Adult':
        if(df['Per Week, how often do you eat Kaya Toast?'][i]) not in Working_Adults:
            Working_Adults[df['Per Week, how often do you eat Kaya Toast?'][i]] = 1
        else:
            Working_Adults[df['Per Week, how often do you eat Kaya Toast?'][i]] += 1
            
    elif (df['What is the age demographic of the customer?'][i]) == 'Elderly':
        if(df['Per Week, how often do you eat Kaya Toast?'][i]) not in Elderly:
            Elderly[df['Per Week, how often do you eat Kaya Toast?'][i]] = 1
        else:
            Elderly[df['Per Week, how often do you eat Kaya Toast?'][i]] += 1            

user_input = input("Please enter the Statistics of the age demographic you want to see (Students / Working Adults / Elderly / All)\n")
print("\n")
if(user_input == "All"):
    print("Showing Statistics for ALL age demographics: ")
    print("\n")
    print("Statistics for Students: ")
    for items in Students:
        print(items,':',Students[items])
    print("\n")    

    print("Statistics for Working Adults: ")
    for items in Working_Adults:
        print(items,':',Working_Adults[items])
    print("\n")

    print("Statistics for the ELderly: ")
    for items in Elderly:
        print(items,':',Elderly[items])
elif(user_input == "Students"):
    print("Showing Statistics for STUDENTS: ")
    print("\n")
    print("Statistics for Students: ")
    for items in Students:
        print(items,':',Students[items])
    print("\n")
    
elif(user_input == 'Working Adults'):
    print("Showing Statistics for WORKING ADULTS: ")
    print("\n")
    print("Statistics for Working Adults: ")
    for items in Working_Adults:
        print(items,':',Working_Adults[items])
    print("\n")
elif(user_input == 'Elderly'):
    print("Showing Statistics for ELDERLY: ")
    print("\n")
    print("Statistics for the Elderly: ")
    for items in Elderly:
        print(items,':',Elderly[items])
    print("\n")
else:
    print("'"+user_input+"'","is an invalid input!")

    
