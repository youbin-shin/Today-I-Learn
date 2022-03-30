from indeed import extract_indeed_pages, extract_indeed_jobs


last_page = extract_indeed_pages()
res = extract_indeed_jobs(last_page)
