get_num=int(input("Enter a number: "))
get_length=int(input("Enter the length: "))
listofmultiplication=[]

for i in range(1,get_length+1):
    push_num=get_num*i
    listofmultiplication.append(push_num)
    print(listofmultiplication)

 

  user_input_str = input("please enter a string: ")
if len(user_input_str) == 0:
    print("There is no str")
 else:
     list_of_str_without_repetition = [user_input_str[0]]
     for i in range(1, len(user_input_str)):
         if user_input_str[i] != list_of_str_without_repetition[-1]:
            list_of_str_without_repetition.append(user_input_str[i])
     print(''.join(list_of_str_without_repetition))
 