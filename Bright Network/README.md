# Job Match Exercise

## Instructions

“In one of our suggested programming languages, please implement a *very simple* recommendations algorithm to match members to their perfect job. Please fetch the required data from the following APIs:

https://bn-hiring-challenge.fly.dev/members.json

https://bn-hiring-challenge.fly.dev/jobs.json

For each member, please print their name and their recommended job(s).We'd like you to spend less than 2 hours on the problem, so your solution will not be perfect (and that's absolutely fine). The purpose is to let us see some of your code, and to give us something to discuss in the technical interview. Please work in a git repository, and share this with us via either a link or zip file. Please also include a brief README which explains the choices you made and the limitations of your approach.

Suggested Languages

* Python
* JavaScript
* TypeScript”

## Solution

The solution for this exercise can be found under `fuzzy_job_match.py`

### Libraries needed

- `$pip install requests`
- `$pip install fuzzywuzzy[speedup]`

### Alternatives considered

1) Do a simple match using the substrings from *job title* and *member bio*.

    Pros: Doesn't need any external libraries.

    Cons: Would not work for words that need lemmatization (example: Design and Designer).

2) **(chosen)** Use fuzzywuzzy library

    Pros: Does partial matching

    Cons: Requires an external library.

3) Manipulate inputs to extract job title from bio.

    Pros: Could improve runtime.

    Cons: More memory needed and more time-consuming to code.

### Justification

After looking at the inputs provided by the `members` and `jobs` URLs and given the 2h suggested timeframe, I decided to use the library [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) since I thought it would be helpful in matching strings. Since the members bio seemed to be in "free text" format, fuzzywuzzy is a useful library to do partial string matching using  `Levenshtein Distance`. The result include a list of matching jobs arranged by "best match" given by the calculated **match score**.

#### Why using the method fuzz.token_set_ratio?

This method allows for partial string matching given that the bio includes more information than just the job title and location, this seemed like the best method to use. 

#### Why setting title_fuzz_ratio_threshold = 40?

After playing with the threshold, I saw that in order to best match each member with their corresponding role, 40 was good threshold to use. This of course can be adjusted depending on how strict we want the match to be.

#### Why not setting a threshold for the location?

Because some of the members do not include location in their bios, or use words such as "outside of London", this make it hard to find a good match for them using the location, therefore I decided to not use a threshold for the location, but instead use a "match score" to consider jobs that matched both title and location. This has the downside that some members would have a suggestion for jobs outside of the location mentioned in their bio, but for this use case it seems more appropiate to provide more matches rather than less.

SIDE NOTES: 
- The run-time of this proposed solution is definitely not optmial and could be further improved if more time is given.
- There would be some examples where the corresponding match score is not ideal (Example Daisy since she wants to relocate from Edinburgh to London, but both jobs in London and Edinburgh result in a 100 score). This could be improved with more advanced libraries that use NLP for example.