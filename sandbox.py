import time
import datetime
import random
import pickle

random.uniform(0.5,1.5)
# for k,i in enumerate(range(0,50, 10)):
#     print(k)
#     time.sleep(1)

# print(datetime.datetime.now().time())
s = "data_dump/jobs_{}.p".format(datetime.datetime.today().strftime('%Y-%m-%d_%H%M'))
pickle.dump(['banana','apple'], open(s, "wb" ))
print(s)