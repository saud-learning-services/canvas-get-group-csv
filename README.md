# Canvas Get Group Csv

⚠️ **You can now export and create groups with a csv using the Canvas interface. We recommend using the Canvas tools instead of the API whenever possible.** For details see the canvas docs ["How do I import a group set"](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-groups-in-a-group-set/ta-p/417799) (when a group is created and you "import", you get details of the current group status as well).

> - name: canvas-get-group-csv
> - ops-run-with: jupyter
> - python>=3.7
> - canvasapi>=2.0.0
> - supports universal environment 🌎
## Summary

**Canvas Get Group Csv** is a Jupyter Notebook and Python application that is used to extract a csv file of group names and associated student user IDs in any Canvas course. The output is a csv called "courseid_course_name_Group Information_datetime.csv" in the folder "output". Application requires the following user inputs:

- Canvas Instance
- Active Canvas Access Token
- Course ID

## Output

### `.csv` detailing

group_id,group_name,course_name,course_id,user_id,user_name

- **group_id** (as it appears on Canvas)
- **group_name** (as it appears on Canvas)
- **course_name** (as it appears on Canvas)
- **course_id** (as it appears on Canvas)
- **user_id** (as it appears on Canvas)
- **user_name** (as it appears on Canvas)

> NOTE: this table contains sensitive information and should **NOT** be distributed or uploaded anywhere

## Important Caveats

- Students unassigned to groups are not included in output.
- Group sets on Canvas are ignored - only group names included in output.
- Duplicate group names are not corrected. 


## Getting Started

### Sauder Operations

_Are you Sauder Operations Staff? Please go [here](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/running-instructions.md) for detailed instructions to run in Jupyter. ("The Project", or "the-project" is "canvas-get-group-csv" or "Canvas Get Group CSV")._


> Project uses **conda** to manage environment (See official **conda** documentation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file))

### First Time
1. Clone **canvas-get-group-csv** repository
1. Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Python 3.7 version)
1. Import environment: `$ conda env create -f environment.yml`
### Every Time
1. Run:
   1. `$ conda activate canvas-get-group-csv`
   1. `$ python src/get_group_csv.py`
   1. Follow instructions in terminal for inputs.
