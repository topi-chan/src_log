## App
###For help run: python main.py --help

Help shows all use cases of the app. In brief, it analyze provided log file for:
- Most frequent IP
- Least frequent IP
- Events per second
- Total amount of bytes exchanged
and saves result in pointed file in json format as: {type of analysis: result}.

## Docker
- Install: $ docker build -t <container_name> .

- Run: $ docker run <container_name> <additional_commands>

## Additional comments
- We assume number of rows to analyze is less than 10 million. For larger files it might be better to use python generators as a method for data acquisition instead of pure pandas (to not overload workspace resources, mainly memory used).
- Assuming most of provided data is correct we didn't make detailed data clearing. Instead, we're omitting it with pandas dataframe on_bad_lines="skip" parameter-argument. Proper data clearing for this amount of data and diversity of its type could be a separate project.
- In case of problems with output data file creation/write try (in a directory you want to save the file to; commands for Linux/macOS): 1/ create empty file with chosen method, e.g. $touch result.json 2/ $ls -l 3/ file should have property rwx (read, write execute) 4/ if it doesn't: $chmod 755 filename (if operation not permitted: $sudo chmod 755 filename) 5/ now indicate created file as an output
