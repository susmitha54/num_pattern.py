'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.
5 5 5 5 5 5 5 5 5   
5 4 4 4 4 4 4 4 5   
5 4 3 3 3 3 3 4 5   
5 4 3 2 2 2 3 4 5   
5 4 3 2 1 2 3 4 5   
5 4 3 2 2 2 3 4 5   
5 4 3 3 3 3 3 4 5   
5 4 4 4 4 4 4 4 5  
5 5 5 5 5 5 5 5 5   

'''

for row in range(9):
    for column in range(9):
        if ((column==0 or column==8 or row==0 or row==8)):
            print('5',end=' ')
        elif ((column==1 or column==7 or row==1 or row==7)):
            print('4',end=' ')  
        elif ((column==2 or column==6 or row==2 or row==6)):
            print('3',end=' ') 
        elif ((column==3 or column==5 or row==3 or row==5)):
            print('2',end=' ')     
        elif ((column==4 or row==4)):
            print('1',end=' ')              
        else:
            print(' ',end=' ')  
            
    print( )