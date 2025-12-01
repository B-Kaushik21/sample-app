with open('sample.txt','r') as file:
    file_data=file.read()
    print(file_data)
    count=file_data.count('\n')
    print("count:",count)