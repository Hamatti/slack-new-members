# Slack New Members

If you're managing a Slack community and want to say hi to new people on a regular interval, say once a week, it can be quite a hassle to figure out who joined after last time and hasn't introduced themselves yet.

So I built this script. It will compare new list of members to and older one and prints out the names that have joined since you ran it last.

To get your list of members, go to `https://[your-slack-name].slack.com/admin` and click the cloud button on the right side of **Manage members** heading to download a CSV file of your members. Then move that into this folder and rename it to `new.csv`.

Then run `python3 diff.py` and you should get a list of new people.

This script then copies the new file to become the next old list to compare against.
