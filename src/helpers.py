
## Functions I seem to use over and over

from interface import shut_down
import unicodedata
import re

def _create_csv(df, output_name):
    print(df.head())
    while True:
        confirmation = input("Your csv will be called: {}\nDo you want to generate this csv from with the data above? (y/n): ".format(output_name))
        
        if confirmation == "y":
            df.to_csv(output_name, index=False)
            print("\n{} created.\nBye!".format(output_name))
            break
        elif confirmation =="n":
            shut_down("\nCsv not created. You can run the script again or exit for no further action.\n")
            break
        else:
            print("Please enter 'y' to accept or 'n' to exit\n")
            continue

def slugify(value):
    """
    Taken and modified from https://github.com/django/django/blob/master/django/utils/text.py
    Convert spaces or repeated ashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = value.replace('/', '-')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


