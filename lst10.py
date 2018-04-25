from lst08 import *

print 'Sorted event log:'

for caseid in sorted(log.keys()):
    log[caseid].sort(key = lambda event: event[-1])
    for (task, user, timestamp) in log[caseid]:
        print caseid, task, user, timestamp
