import sys
import clipboard
import json

SAVE_DATA = 'clipboard.json' # create the file first than the def functions

def save_data(filepath, data): # Creating the filepath with parameter data
    with open(filepath,"w") as f: # You are writing a file/data in Json for the clipboard
        json.dump(data, f) # You are dumping the file to json to be converted


def load_data(filepath): # Loading the file
    try:
        with open(filepath, 'r') as f: # Using try to open filepath
            data = json.load(f) # data is stored as the file saved to clipboard.
        return data # returning the data to clipboard file
    except:
        return {} # return an empty string


if len(sys.argv) == 2: # this is the script(1st argument) and command(2nd argument)
    # so when you run len(sys.argv) you main.py and the command which is 2 arg.
    command = sys.argv[1] # this is the command you are typing in to save to load data.
    data = load_data(SAVE_DATA) # Data is the two def functions of the file.


    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVE_DATA, data)
        print("Data saved")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("key does not exist")
    elif command == "list":
        print(data)
    else:
        print('unknown command')
else:
    print('Please pass in the correct command')

# This is you accessing the file path your in the system.
# After you type python in the terminal with the file your currently in,
# you are passing arguments to the file in a list.