## App

### For help run: python main.py --help

Help shows all use cases of the app. In brief, it analyze provided log file for (commands in parentheses):
- Most frequent IP (mfip)
- Least frequent IP (lfip)
- Events per second (eps)
- Total amount of bytes exchanged (bytes)

and saves result in pointed file in json format as: {type of analysis: result}.

Input file/files should be of plain-text type and output file of json type

For running program locally without Docker: 
https://docs.python.org/3/library/venv.html
- Create venv: $ python3 venv /venv/
- Activate venv: $ venv/bin/activate or if permission denied: $ . venv/bin/activate
- Install libraries: pip install -r requirements.txt
- To run program activate venv and run, from logs_app directory: $ python main.py --help
- To deactivate env: $ deactivate

## Docker
- Install (execute in directory with dockerfile): $ docker build -t <container_name> .

- Run: $ docker run <container_name> <additional_commands> (e.g. --help)
- Run with passing log file (sample directory from PyCharm standard; container name: test_log): 

  To make an operation directly on a container and then copy on local (this way you're running a container only once): 
- $ docker run -it -v /Users/username/PycharmProjects/src_log/access.log:/access.log /Users/username/PycharmProjects/src_log/result.json:/result.json test_log mfip access.log result.json

  To save on a container and then copy on local:

- $ docker run -it -v /Users/username/PycharmProjects/src_log/access.log:/access.log test_log mfip access.log result.json

    or
- $ docker run -it --mount src=/Users/username/PycharmProjects/src_log/logs_app/access.log,target=/access.log,type=bind test_log mfip access.log result.json
- Copy results from container to local: $ docker cp test_log:/result.json  /Users/username/PycharmProjects/src_log/logs_app/result.json


## Additional comments
- Sample file: https://www.secrepo.com/squid/access.log.gz
- Run pytest from src_log/logs_app level.
- Project is written with assumption of usage by user without or with very basic prior knowledge of Python but with basic Docker knowledge (that's how I understood target group for such tools at the interview).
- Among other reasons that's why Tests are basic, some of them are more E2E than unit tests in nature, I've put more focus on manual testing.
- Since main.py is merely for calling other functions and visual output (which is aesthetically subjective). That module could be replaced with, for example, only "sys argv" approach, so I did not put much emphasis on commenting it.
- I assume number of rows to analyze is less than 10 million. For larger files it might be better to use python generators as a method for data acquisition instead of pure pandas (to not overload workspace resources, mainly memory used).
- Docker provides python main.py command from entrypoint.
- Code was formatted according to Black and Isort libraries standard.
- Assuming most of provided data is correct we didn't make detailed data clearing. Instead, we're omitting it with pandas dataframe on_bad_lines="skip" parameter-argument. Proper data clearing for this amount of data and diversity of its type could be a separate project.
  Due to that, I'm trying to read imput data with many conditional statements, logging what could possibly be wrong with the file. Load_input_data could be atomized much further (e.g. for better testing, but I decided to keep it as a single flow, for sake of more consistent explanation "what's going on" in the side comments).
- Since requirements insisted on strong "in code" comments strategy, detailed readme, and as I used typehints and created --help I decided to not add docstrings in the code, to not "overkill" the code with commentary section.
- In case of problems with output data file creation/write try (in a directory you want to save the file to; commands for Linux/macOS): 1/ create empty file with chosen method, e.g. $touch result.json 2/ $ls -l 3/ file should have property rwx (read, write execute) 4/ if it doesn't: $chmod 755 filename (if operation not permitted: $sudo chmod 755 filename) 5/ now indicate created file as an output
