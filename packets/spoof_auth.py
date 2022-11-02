#!/usr/bin/python3.11
from sys import argv

r = []
for i in range(1, 5):
    try:
        r.append(argv[i])
    except(IndexError):
        r.append(None)

if r[0] != None and r[1] != None:
    usr = r[0]+' '+r[1] or 'a b'
else:
    usr = 'k ernel'

if r[2] != None:
    job = r[2]
else:
    job = 'NTKERNEL'

if r[3] != None:
    access = r[3]
else:
    access = '34;69'

# 1. Login as any user, save spoofed login packet as a file at /mnt/term
# 2. logout
# 3. term_send     Spoof user auth, login
# 4. su            Create auth challenge
# 5. term_send     Spoof superuser auth, login as superuser


print(f"user: {usr}\njob: {job}\naccess: {access}")
print(f"payload: echo registered={usr}|nassignment={job}|naccess={access} ^ /mnt/term/f")
#print(f"echo registered={usr}|nassignment={job}|naccess=34^ /mnt/term/f",end='')
