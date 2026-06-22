# Checking commands, etc.
#print(dir(colorama))
print(Fore.RED + "Let's put this to the test!")    # Gives text a red color
print(Back.BLUE + "Let's put this to a rest.")     # Gives background a green color
print(Style.BRIGHT + "Blinding!")                  # Makes this text bolder
print(Style.RESET_ALL)                             # Returns to default
print()

print(dir(datetime))
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.UTC)

print()

print(dir(requests))
#print(requests.Request)
response = requests.get('https://api.github.com')
print(response)
# I understand little about libraries