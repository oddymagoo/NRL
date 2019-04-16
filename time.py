import time

# 86,400 x 7
week = 604800
now = time.time()
commence_time =  1554368700

local_time = time.ctime(now)
future_time = time.time() + 604800

print("Local time:", local_time)
print ("One Week:", time.ctime(future_time))
print ("Commence:", time.ctime(commence_time))

