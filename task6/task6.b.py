def create_file_and_count_occurences():
    file_name=input("Enter the filename to create:")
    with open(file_name,'w')as file:
        print("Enter the contents of the file (press Enter to finish):")
        while True:
            line=input()
            if not line:
                break
            file.write(line+'\n')
    print("\n contents of the file:")
    with open(file_name,'r')as file:
        print(file.read())
    letter=input("\n enter the letter to create occurrences:")
    with open(file_name,'r')as file:
        content=file.read()
        count=content.count(letter)
        print(f"\n The letter '{letter}' occur '{count}' times in the file.")
create_file_and_count_occurences()
