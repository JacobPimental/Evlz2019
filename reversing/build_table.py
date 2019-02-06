import subprocess

map = {}

rainbow_table = '@!"#$%&\'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^ _abcdefghijklmnopqrstuvwxyz{|}~'

for char in rainbow_table:
    info = subprocess.run('echo "'+char+'" | ./smol-big', shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = info.stdout.split(b'\n')
    binary = stdout[-2].decode('utf-8')
    print("%s is %s" % (char, binary))
    map[binary] = char

cur_str = ''
f = open('3337a0a1c85ddbc67ae000f747cfd7e7')
words = f.read()

flag = ''

for b in words:
    cur_str += b
    if cur_str in map.keys():
        flag += map[cur_str]
        cur_str = ''

print(flag)
