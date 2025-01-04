import subprocess
import datetime
import os

# extract script dir
script_dir = os.path.dirname(os.path.abspath(__file__))
# join dir + file
file_path = os.path.join(script_dir,"text.txt")
print(os.chdir(script_dir))

def read_number():
    with open(file_path,"r") as file:
        return int(file.read()) 

def write_number(number): 
    with open(file_path,"w") as file:
        file.write(str(number)) 


def git_push_changes():
    try:

        # Run git add . in "CLI"
        obj = subprocess.run(['git','add','.'])
        # current date
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        message = f'Contribution day: {date}'
        # Commit the changes
        subprocess.run(['git','commit','-m',message])
        # Push changes to repository
        subprocess.run(['git','push'])
    except subprocess.CalledProcessError as e:
        print(f"Error {str(e)}")
    

def main():
    try:
        current_number = read_number() 
        number_to_change = current_number + 1 
        add_number = write_number(number_to_change)
        git_push_changes()
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()