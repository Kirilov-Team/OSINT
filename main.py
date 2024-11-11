import os
import time
from googlesearch import search

os.system("cls")
print("1 : All appearances on websites about a person")
print("2 : All files about person")
print("3 : All appearances about an certain subject")
print("4 : All files about an certain subject")
choice = input("Choose ->  ")

choice = int(choice)

if choice == 1:
    person = input("Person : ")
    query = f'"{person}" intext:"{person}"'

if choice == 2:
    person = input("Person : ")
    query = f'"{person}" filetype:txt OR filetype:pdf OR filetype:docs OR filetype:bat OR filetype:exe OR filetype:zip OR filetype:7z'

if choice == 3:
    theme = input("Theme : ")
    query = f'{theme} intext:{theme}'

if choice == 4:
    theme = input("Query : ")
    filetype = input("Filetype : ")
    query = f'{theme} filetype:{filetype}'

os.system("cls")
print("Starting search sequence... (do not close)")

num = 0
done = False

while not done:
    try:
        with open('websites.txt', 'w') as a:
            for i in search(query):
                print(i)
                num += 1
                time.sleep(0.1)
                a.write(i)
                a.write("\n")
            print("Success!")
            done = True
    except:
        os.system("cls")
        print("Google cut the data flow, please do not close the program, after a few minute we will continue the scraping!")

os.system("cls")
print("Script finished!")
print(f"Found {num} URLs")
print("Results saved to : websites.txt")

end = input("Press Enter To Close")
os.system("websites.txt")
