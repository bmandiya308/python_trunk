import subprocess_ops

execution = subprocess_ops.Popen("dir", shell=True, stdout=subprocess_ops.PIPE)
subprocess_return = execution.stdout.read()
#print(subprocess_return)
for i in str(subprocess_return).split("\\r\\n"):
    print(i)