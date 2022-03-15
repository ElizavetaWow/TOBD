from mean_steps_for_file_mp import mean_steps_for_file_mp

def worker(in_q, out_q):
    for task in iter(in_q.get, 'STOP'):
        d = mean_steps_for_file_mp(task)
        out_q.put(d)
