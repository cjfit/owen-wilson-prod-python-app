## Sample Owen Wilson Prod-Ready Python App

Consumes the Owen Wilson Wow API (https://owen-wilson-wow-api.onrender.com/).
An initial CSV input file of movie names, release years, and IMDb ratings is at data/input.csv. This data is combined with "wow" data and written6 to a new CSV.
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