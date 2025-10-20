def count_even_odd(number):
    even_count=0
    odd_count=0   
    for num in number:  
       if num%2==0:
          even_count+=1
       else:
          odd_count+=1
    return even_count,odd_count
input_numbers=input("enter a series of numbers separeted by spaces:")
numbers=list(map(int,input_numbers.split()))
even_count,odd_count=count_even_odd(numbers)
print("number of even number:",even_count)
print("number of odd number:",odd_count)
                                                                                                                                                                                                                                           def count_even_odd(number):
                                                                                                                                                                                                                                  even_count=0
                                                                                                                                                                                                                                  odd_count=0
                                                                                                                                                                                                                                      for num in number:
                                                                                                                                                                                                                                       if num%2==0:
                                                                                                                                                                                                                                        even_count+=1
                                                                                                                                                                                                                                     else:
                                                                                                                                                                                                                                        odd_count+=1
                                                                                                                                                                                                                                     return even_count,odd_count
                                                                                                                                                                                                                             input_nummber=input("enter a series of number separated by spaces:")
                                                                                                                                                                                                                             number=list(map(int,input_number.split()))
                                                                                                                                                                                                                             even_count,odd_count=count_even_odd(number)
                                                                                                                                                                                                                             print("Number of even number:",even_count)
                                                                                                                                                                                                                             print("Number of odd number:",odd_count)            
                                                                                                                                                                                                                                                                                                                                                                                                 
