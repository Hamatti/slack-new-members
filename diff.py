from collections import namedtuple
import csv
import datetime
import os
import shutil

# These are the column headers for Slack's members list as of Feb-10-2020.
# If Slack changes their format, this needs to be updated.
HEADERS = ['username', 'email', 'status',
           'active', 'twofa', 'sso', 'userid', 'fullname', 'displayname']

BACKUP = 'backup.csv'
EXISTING = 'existing.csv'
NEW = 'new.csv'

Person = namedtuple('Person', HEADERS)


def exists(lst, person):
    matches = [p for p in lst if p.email == person.email]
    return len(matches) > 0


def read_data(fname):
    data = []
    with open(fname, 'r') as f:
        for person_data in csv.reader(f):
            try:
                person = Person(*person_data)
                data.append(person)
            except TypeError as err:
                print(f'ERROR')
                print(err)
                print(person_data)
    # Skip headers
    return data[1:]


if __name__ == '__main__':
    # EXISTING needs to exist so create it if it doesn't
    if not os.path.isfile(EXISTING):
        with open(EXISTING, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

    try:
        print(f'Creating a backup file {BACKUP}')
        shutil.copyfile(EXISTING, BACKUP)
    except:
        print(f'Failed to create a backup.')

    new_people = read_data(NEW)
    existing_people = read_data(EXISTING)

    for person in new_people:
        # Skip empty lines and deactivated accounts
        if not person or person.status != 'Member':
            continue

        # Skip people who already are part of older list
        if exists(existing_people, person):
            continue

        print(
            f'user: {person.username}\nemail: {person.email}\ndisplayname: {person.displayname}\n')

    # Overwrite the old file with new file
    os.rename(NEW, EXISTING)
