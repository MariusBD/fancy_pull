# Daily Push Github

This python script increments a number in a text file commits and push the changes to github automatically daily, using Task Scheduler from Windows.

1. Clone repository:
   
```
git clone https://github.com/MariusBD/fancy_pull.git
```

2. Run script

```
python git_push.py
```

3. Setup your Task Schedule:
   - Open Task Scheduler and create new task
   - Open Actions: fill the fields: script, args, start.
     script: full path of python.exe
     args: script name (git_push.py)
     start: full directory of the script.
   - Triggers: Schedule your script

     Once you configured this part your are good to go, you can force your task to run by pressing "Run" even if it's not scheduled.

Now you have a daily streak script on github!! 



