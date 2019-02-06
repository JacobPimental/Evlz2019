import subprocess

f = open('shroud_strings')
lines = f.readlines()

map = {}
'''
for line in lines:
    info = subprocess.run(('echo "WaduhEKK wAdUhEkK WADuhEKK '+line.strip()+
                          ' WaDuhEKk waduHeKk wAdUhEkK WaduhekK" | ./shroud'), shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = info.stdout
    print('RUNNING: ' + line.strip())
    print(stdout)
    print('----------------------------------------------------------------------')
'''

rainbow =('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\\#_'+
          '%;\'()*+,-./:? ')

for i in range(len(rainbow)):
    map[rainbow[i]] = lines[i].strip()

map[' ']= 'WADuHEkK'
cmd = input('input command: ')
while cmd != 'exit':
    wadu = ''
    for char in cmd:
        wadu += map[char]+' '
    print(wadu)
    cmd = input('input command: ')



