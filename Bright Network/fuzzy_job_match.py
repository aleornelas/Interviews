import requests
from fuzzywuzzy import fuzz

members_url = 'https://bn-hiring-challenge.fly.dev/members.json'
jobs_urls = 'https://bn-hiring-challenge.fly.dev/jobs.json'
title_fuzz_ratio_threshold = 40

members = requests.get(members_url)
jobs = requests.get(jobs_urls)

job_matches = {}

def job_match(job, member):
    title_fuzz_ratio = fuzz.token_set_ratio(job['title'], member['bio'])
    location_fuzz_ratio = fuzz.token_set_ratio(job['location'], member['bio'])
    match_score = (title_fuzz_ratio + location_fuzz_ratio) / 2.0

    if title_fuzz_ratio > title_fuzz_ratio_threshold:
        if member['name'] in job_matches:
            job_matches[member['name']].append((match_score, job))
        else:
            job_matches[member['name']] = [(match_score, job)]


def print_matches():
    for name,matches in job_matches.items():
        print(name)
        matches.sort(key=lambda x: x[0], reverse=True)
        for match in matches:
            print('Job: ', match[1], ' Match Score: ', match[0])
        print()

def main():
    for member in members.json():
        for job in jobs.json():
            job_match(job, member)
    
    print_matches()

if __name__ == "__main__":
    main()
