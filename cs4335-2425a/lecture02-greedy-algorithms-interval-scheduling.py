jobs = [
    (0, 10),
    (3, 4),
    (2, 8),
    (1, 5),
    (4, 5),
    (4, 8),
    (5, 6),
    (7, 9),
]  # (start_time, finish_time)

# Sort jobs by finish time
sorted_jobs = sorted(jobs, key=lambda x: x[1])
selected_jobs = []

for job in sorted_jobs:
    # if job is compatible with the selected jobs
    if not selected_jobs or job[0] >= selected_jobs[-1][1]:
        # then add it to the selected jobs
        selected_jobs.append(job)

print(selected_jobs)
