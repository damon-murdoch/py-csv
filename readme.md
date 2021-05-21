# py-csv
## Python CSV to Object Reader
### Created by Damon Murdoch 

## Description
py-csv is a small python script developed for the purpose of cleanly importing the content of comma-seperated values (csv) files to the powershell object format. Currently only csvs with headers are handled, however in future it is planned to support no-header files also. The input and output formats will be described below.

### Input Content

#### Input Command
```bash 
python reader.py players.csv
```

#### Input File Contents
```csv
Name,Wins,Losses,Available
Justice,1,0,1
Damon,0,1,1
```

### Output Content
```json
{'Justice': {'Wins': '1', 'Losses': '0', 'Available': '1'}, 'Damon': {'Wins': '0', 'Losses': '1', 'Available': '1'}}
```

## Future Changes
A list of future planned changes are listed below.

| Change Description | Priority |
| --------------------------- | -------- | 
| Handle csvs without headers | High     |

### Problems or improvements
If you have any suggested fixes or improvements for this project, please 
feel free to open an issue [here](issues).

