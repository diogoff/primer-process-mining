from lst02 import *

log.sort(key = lambda event: (event[0], event[-1]))

print 'Sorted event log:'

for (caseid, task, user, timestamp) in log:
    print caseid, task, user, timestamp
