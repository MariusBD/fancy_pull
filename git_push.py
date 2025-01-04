import subprocess
import datetime
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    with open("text.txt","r") as file:
        return int(file.read()) 

def write_number(number): 
    with open("text.txt","w") as file:
        file.write(str(number)) 


def git_push_changes():
    try:
        # Run git add . in "CLI"
        obj = subprocess.run(['git','add','.'])
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        message = f'Contribution day: {date}'
        # Commit
        subprocess.run(['git','commit','-m',message])
        # Push to repository
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