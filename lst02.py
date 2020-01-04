f = open('eventlog.csv', 'r')

log = []

for line in f:
    line = line.strip()
    if len(line) == 0:
        continue
    parts = line.split(';')
    caseid = parts[0]
    task = parts[1]
    user = parts[2]
    timestamp = parts[3]
    event = (caseid, task, user, timestamp)
    log.append(event)
    
f.close()

for (caseid, task, user, timestamp) in log:
    print(caseid, task, user, timestamp)
