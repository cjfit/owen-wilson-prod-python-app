## Sample Owen Wilson API Prod-Ready Python App

Consumes the Owen Wilson Wow API (https://owen-wilson-wow-api.onrender.com/).
An initial CSV input file of movie names, release years, and IMDb ratings is at data/input.csv. This data is combined with "wow" API data and written to a new CSV.

### Example Input (data/input.csv)

| Movie Name   | Release Year | Rating | id  |
|--------------|-----|--------|-----|
| Cars         | 2006 | 7.2    | 11  |
| The Darjeeling Limited | 2007 | 7.2    | 13  |
| Marley & Me | 2008 | 7.0    | 15  |
| The Internship | 2013 | 6.3    | 22  |


### Example Output

| Movie Name   | Release Year | Rating | id  |  Total Wows  |  Full Line  |
|--------------|-----|--------|-----|---|---|
| Cars         | 2006 | 7.2    | 11  |5|Wow! What is this place?
| The Darjeeling Limited | 2007 | 7.2    | 13  |1|Wow. Right?
| Marley & Me | 2008 | 7.0    | 15  |3|Four for four. Wow.
| The Internship | 2013 | 6.3    | 22  |5|Wow! Seven projects.



### Running tests
Navigate to the tests/ directory and run `pytest`
### Instructions for use

The following should be run from this root directory.
1. Ensure this containing folder is in your $PATH, or move it there. 
2. Run `chmod 755 wow_report` to make the bash script executable.
3. Create a new virtual env: `python3 -m venv venv`
4. Activate the virtual env: `source venv/bin/activate` 
5. Install dependencies: `pip install -r requirements.txt `
4. Invoke the script as such from the terminal: `wow_report data/input.csv output.csv`