import sys

arg = sys.argv

print(arg)

if len(arg) > 3:
    print("exceeding limit...")
    exit(0)
if arg[2].find('--message') != -1:
    if arg[2].find('=') != -1:
        print(arg[2][arg[2].find('=') + 1 : ])

else:
    print("No message supplied in wrong format..")
