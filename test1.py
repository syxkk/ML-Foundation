import time
start=time.time()
s=0
for i in range(100):
   s+=i
time.sleep(10)
end=time.time()
print(end-start)