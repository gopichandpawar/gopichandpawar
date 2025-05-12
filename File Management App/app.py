#File Management App
import os 

def create_file(filename):
    try:
        with open(filename,"x")as f:
            print(f"file name {filename} created successfully")
    
    except FileExistsError:
        print(f"file name {filename} already exist")
    
    except Exception as e:
        print("An error Occurred")
    
def view_all_file():
    files = os.listdir()
    if not files:
        print("no file found")
    else:
        print("files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename} has been delete successfully")
    
    except FileExistsError:
        print("file not found")
    
    except Exception as e:
        print("An error occurred")
    
def read_file(filename):
    try:
        with open(filename,"r")as f:
            data = f.read()
            print(f"data of {filename} :\n{data}")
    
    except FileExistsError:
        print(f"{filename} does not exist")
    
    except Exception as e:
        print("An error occurred")

def edit_file(filename):
    try:
        with open(filename,"a")as f:
            data = input("enter data to add =")
            f.write(data + "\n")
            print(f"data added to {filename} successfull")
    
    except FileExistsError:
        print(f"{filename} does not exist")
    
    except Exception as e:
        print("An error occurred")
    
def main():
    while True:
        print("\nFile Management App")
        print("1, create file")
        print("2, view all file")
        print("3, delete file")
        print("4, read file")
        print("5, edit file")
        print("6, exit")

        choice = input("enter you choice =")

        if(choice == '1'):
            filename = input("enter filename to create =")
            create_file(filename)
        
        elif(choice == '2'):
            view_all_file()

        elif(choice == '3'):
            filename = input("enter filename to delete file =")
            delete_file(filename)

        elif(choice == '4'):
            filename = input("enter file name to read file =")
            read_file(filename)

        elif(choice == '5'):
            filename = input("enter filename to edit file =")
            edit_file(filename)
        
        elif(choice == '6'):
            print("closing the app...!")
        
        else:
            print("invalid input")

if __name__ == "__main__":
    main()