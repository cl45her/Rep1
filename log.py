raw_logs = [104, 101, 102, 101, 105, 103, 104, 108, 102]
processed_ids = [101, 102, 103]
raw_logs = set(raw_logs)
raw_logs = set.difference(raw_logs,processed_ids)
new_ind = sorted(raw_logs)
print(new_ind)