#Menu bar
while True:
    print("---Text File Manager---")
    #User will choose any one option
    print("1. Create a file")
    print("2. Read a file")
    print("3. Write a file")
    print("4. Append a file")
    print("5. Delete a file")
    print("6. Exit")
    # For Exception handling
    try:
     choice = int(input("Enter your choice")) # option will be selected
    # To create a file
     if choice==1:
      text= input("Enter your text")
      file = open("data.txt","w") 
      file.write(text)
      file.close()
      print("Data Saved Succesfully")

     elif choice==2:
        # To read a file
        try:
         file = open("data.txt","r") 
         print(file.read())
         file.close()
        except FileNotFoundError:
          print("File is not found") 

     elif choice == 3:
       # To write in file
       file = open("data.txt","w") 
       text = input("Enter your text")
       file.write(text)
       file.close()
       print("Data Saved Succesfully")

     elif choice == 4:
       # To append in file
       file = open("data.txt","a") 
       text = input("Enter your text")
       file.write(text)
       print("Data Saved Succesfully")
       file.close()

     elif choice == 5:
       # To delete a text from file
       file = open("data.txt","r+") 
       file.truncate()  
       file.close()
       print("Data Deleted From File")       

     elif choice==6:
        # To exit
        print("Exit")
      
     # For any invalid number
     else:
      print("Invalid Choice...")
      # Exception will be handled here
    except FileNotFoundError :
      print("File Not Found")
    except ValueError:
      print("Enter a Valid Value") 
    except Exception as e:
      print("Error",e)   