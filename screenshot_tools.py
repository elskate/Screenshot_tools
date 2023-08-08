import imgkit
import os
import signal

data = open('domains.txt')
list_of_domains = []
for element in str(data.read()).split('\n'):
    list_of_domains.append(element)
os.chdir('screens')
for element in list_of_domains:
    try:
        signal.alarm(10)
        imgkit.from_url(element, f'{element}.jpg')
        signal.alarm(0)
    except Exception:
        print(f'Cannot screen {element}')