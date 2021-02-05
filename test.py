import subprocess as sp

process = sp.Popen('python hello.py'.split(), stdout=sp.PIPE, stderr=sp.PIPE)
out, err = process.communicate()

if 'hello' in out.lower():
    exit(0)
else:
    exit(1)
