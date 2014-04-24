from subprocess import call

call(["source pythonwork/envs/dannyswebsite/bin/activate"])
call(["python pythonwork/dannyswebsite/manage.py", "runserver"])