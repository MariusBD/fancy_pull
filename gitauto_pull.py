import os
import subprocess
import datetime

def read_number():
    with open("text.txt","r") as file:
        return int(file.read()) # --> retorna un int

def write_number(number): #recibe el nuevo numero
    with open("text.txt","w") as file:
        file.write(str(number)) # --> pasa el nuevo numero a string

current_number = read_number() # --> retorna un unico numero y lo almacena
number_to_change = current_number + 1 # --> suma + 1 a ese numero
add_number = write_number(number_to_change) # --> añade el numero del tipo int, y lo escribe en string

# TODO : ACTUALIZAR LOS CAMBIOS DE LA CARPETA, GIT ADD, GIT COMMIT -M "NAME", GIT PUSH  TO REPOSITORY

def git_commit():
    obj = subprocess.run(['git','add','.'])
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    message = f'Contribution day: {date}'
    subprocess.run(['git','commit','-m',message])
    print(message)
    

git_commit()

# for i in range(5):
#     current_number = read_number()
#     next_number = current_number + 1
#     write_number(next)