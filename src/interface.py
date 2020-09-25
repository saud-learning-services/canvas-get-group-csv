"""
GROUP CSV: interface & utl
authors:
@markoprodanovic
last edit:
September 24, 2020
"""

import getpass
from canvasapi import Canvas
from termcolor import cprint
import sys
import settings


def print_error(msg):
    """ Prints the error message without shutting down the script
    Args:
        msg (string): Message to print before continuing execution
    """
    cprint(f'\n{msg}\n', 'red')


def shut_down(msg):
    """ Shuts down the script.
    Args:
        msg (string): Message to print before printing 'Shutting down...' 
                      and exiting the script.
    """
    cprint(f'\n{msg}\n', 'red')
    print('Shutting down...')
    sys.exit()

def get_user_inputs():
    """Prompt user for required inputs. Queries Canvas API throughout to check for
    access and validity errors. Errors stop execution and print to screen.
    Returns:
        Dictionary containing inputs
    """

    # prompt user for url and token
    url = input('Please enter your url: ')
    token = getpass.getpass('Please enter your token: ')
    auth_header = {'Authorization': f'Bearer {token}'}

    # Canvas object to provide access to Canvas API
    canvas = Canvas(url, token)

    # get user object
    try:
        user = canvas.get_user('self')
        cprint(f'\nHello, {user.name}!', 'green')
    except Exception:
        shut_down(
            """
            ERROR: could not get user from server.
            Please ensure token is correct and valid and ensure using the correct instance url.
            """
        )

    # get course object
    try:
        course_id = input('Course ID: ')
        course = canvas.get_course(course_id)
    except Exception:
        shut_down(
            f'ERROR: Course not found [ID: {course_id}]. Please check course number.')


    # prompt user for confirmation
    _prompt_for_confirmation(user.name, course.name)

    settings.course = course
    # return inputs dictionary
    return(url, course_id)


def _prompt_for_confirmation(user_name, course_name):
    """Prints user inputs to screen and asks user to confirm. Shuts down if user inputs
    anything other than 'Y' or 'y'. Returns otherwise.
    Args:
        user_name (string): name of user (aka. holder of token)
        course_name (string): name of course returned from Canvas
    Returns:
        None -- returns only if user confirms
    """
    cprint('\nConfirmation:', 'blue')
    print(f'USER:  {user_name}')
    print(f'COURSE:  {course_name}')
    print('\n')

    confirm = input(
    'Would you like to continue using the above information? [y/n]: \n')

    if confirm == 'y' or confirm == 'Y':
        return
    elif confirm == 'n' or confirm == 'N':
        shut_down('Exiting...')
    else:
        shut_down('ERROR: Only accepted values are y and n')            