#All Modules
import math
import statistics
import json


#All Variables



#All Functions

def create_list():
    List_init = []
    number_ele_List = int(input("please enter number elements to be available in list"))  
    for element in range(number_ele_List):
        element_n = int(input("please enter the element: "))
        List_init.append(element_n)
    return List_init


def append_list(List):
    element_to_be_inserted = int(input("Please enter the element to be inserted: "))
    List.append(element_to_be_inserted)
    return List

def pop_list(List):
    #Two different types of pop operations
    return List
    
def len_list(List):
    return len(List)




print("Welcome to Data structure calculator")

print("Please select any operation to proceed \n1.List \n2.Tuple \n3.Set \n..... ")

data_input = int(input("please enter a number between 1 and 4 "))

if data_input == 1:
                 print("Welcome to List operations ")
                 print("Create a List for proceeding List Operations")
                 List_main = create_list()
                 print("The created list is ", List_main)
                 print("Please select any one List operation to proceed (Any number between 1-15)")
                 print("1. Append \n 2. pop \n 3. len ......")

                 List_operation_input = int(input("please enter any one number ..."))

                 if List_operation_input == 1:
                                        output_append = append_list(List_main)
                                        print("The output after append operations is ", output_append)
                 elif List_operation_input == 3:
                                        output_len = len_list(List_main)
                                        print("The output after len operations is ", output_len)

elif data_input == 2:
                print("Welcome to Tuple Oprations")
                             
                 
                    
                
                 
