from indeed import get_jobs as get_indeed_jobs
from incruit import get_jobs as get_incruit_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs('python')
incruit_jobs = get_incruit_jobs()
jobs = indeed_jobs + incruit_jobs
save_to_file(jobs)
