import pandas as pd
from canvasapi import Canvas
import getpass
import sys
from IPython.display import display, HTML
from helpers import _create_csv, slugify
from datetime import datetime
from interface import get_user_inputs, shut_down
from dotenv import load_dotenv
import settings

# for printing neatly formatted objects (used for debugging)
load_dotenv()

def get_group_data(course):
    # get groups from course
    try:
        groups = course.get_groups(per_page=50)

        try:
            groups[0]
        except IndexError:
            shut_down(f'No groups found in the course {course.name}.')

        all_groups = []

        for group in groups:
            
            users_list = group.get_users()
            
            for user in users_list:
                group_dict = {}
                group_dict['group_id'] = group.id
                group_dict['group_name'] = group.name
                #group_dict['group_created_at'] = group.created_at
                group_dict['course_name'] = course.name
                group_dict['course_id'] = course.id
                #print(group, user)
                group_dict['user_id']= user.id
                group_dict['user_name']= user.name
            
                all_groups.append(group_dict)

            # membership_list = group.get_memberships()
            # for member in membership_list:
            #     group_dict['moderator'] = member.moderator
            #     #group_dict['workflow_state'] = member.workflow_state
            #     #group_dict['membership_id'] = member.id
            
        return(pd.DataFrame(all_groups))

    except Exception as e:
        shut_down("Something went wrong: {}".format(str(e)))

def main():

    settings.init()
    url, course_id = get_user_inputs()
    
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M%S")

    df = get_group_data(settings.course)
    
    display(df)
    output_name = "{}/{}_{}_Group_Information_{}.csv".format("output", course_id, slugify(settings.course.name), timestamp)
    _create_csv(df, output_name)

if __name__ == "__main__":
    # execute only if run as a script
    main()