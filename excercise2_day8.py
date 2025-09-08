import time
timestamp=time.strftime('%H:%M:%S',time.localtime(time.time()))
if timestamp < '12:00:00':
    print("Good Morning!")
elif timestamp < '18:00:00':
    print("Good Afternoon!")
else:
    print("Good Evening!")
