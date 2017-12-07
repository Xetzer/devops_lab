'''Usage: python gitch.py -s -f -l -o -c -a -d -n -p Xetzer -u alenaPy -r devops_lab'''
import getpass
import argparse
import datetime
import calendar
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--puller', required=True, help='Pull request author, mandatory paramether')
parser.add_argument('-u', '--user', required=True, default='alenaPy', help='github.com repository owner, mandatory paramether')
parser.add_argument('-r', '--repo', required=True, default='devops_lab', help='github.com repository, mandatory paramether')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-s', '--stats', action='store_true', help='Overall merged/closed stats')
parser.add_argument('-f', '--find', action='store_true', help='Find all pull requests from specified user')
parser.add_argument('-l', '--lifetime', action='store_true', help='Lifetimes of active requests from specified user')
parser.add_argument('-o', '--openday', action='store_true', help='Days of week when requests from specified user were opened')
parser.add_argument('-c', '--closeday', action='store_true', help='Days of week when requests from specified user were closed')
parser.add_argument('-a', '--additions', action='store_true', help='Number of additions in requests from specified user')
parser.add_argument('-d', '--deletions', action='store_true', help='Number of deletions in requests from specified user')
parser.add_argument('-n', '--number', action='store_true', help='Number of comments in requests from specified user')

args = parser.parse_args()

puller = str(args.puller)
usergit = str(args.user)
repo = str(args.repo)

'''
s = str(args.stats)
f = str(args.find)
l = str(args.lifetime)
o = str(args.openday)
c = str(args.closeday)
a = str(args.additions)
d = str(args.deletions)
n = str(args.number)
'''

# Getting authorization paramethers
username = input("GitHub username: ")
password = getpass.getpass("Password: ")
authen = (username, password)

# Defining useful variables
url = "https://api.github.com/repos/" + usergit + "/" + repo + "/pulls?state=all"
urlp = "https://api.github.com/repos/" + usergit + "/" + repo + "/pulls/"
curd = datetime.date.today()
curt = str(datetime.datetime.now().time()).split(':')
req = requests.get(url, auth=authen)
numpuls = int((req.json()[0]["number"]))
numpages = numpuls // 30 + 1
total = 0
closed = 0
merged = 0

# JSON retrieving
req = requests.get(url, auth=authen)
rej = req.json()
while "next" in req.links.keys():
    nextp = req.links["next"]["url"]
    req = requests.get(nextp, auth=authen)
    rej = rej + req.json()

if args.stats:
    for i in range(numpuls):
        if rej[i]["state"] == "closed":
            closed += 1
        if rej[i]["merged_at"]:
            merged += 1

    print("\n" + "Closed requests: ", closed)
    print("Merged requests: ", merged)
    print("Overall merged/closed requests ratio, %: ", round((merged / closed) * 100, 2))

if args.find:
    print("\n" + "Requests made by " + puller + ":")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller:
            print("Request number " + str(rej[i]["number"]) + ", created on " + rej[i]["created_at"].split('T')[0])
            total += 1
    print("Total " +  str(total) + " pull requests from user " + puller + ".")

if args.lifetime:
    print("\n" + "Lifetimes of active requests from " + puller + ":")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller and rej[i]["state"] == "open":
            opend = (rej[i]["created_at"].split("T")[0]).split("-")
            opend = datetime.date(int(opend[0]), int(opend[1]), int(opend[2]))
            if opend == curd:
                print(("Request number " + str(rej[i]["number"]) + " was opened today"))
            else:
                diffd = str(curd - opend).split()[0]
                print(("Request number " + str(rej[i]["number"]) + " was opened {} day(s) ago").format(diffd))

if args.openday:
    print("\n" + "Days of week when requests from " + puller + " were opened:")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller and rej[i]["state"] == "open":
            dopen = (rej[i]["created_at"].split("T")[0]).split("-")
            dopen = (calendar.day_name[datetime.date(int(dopen[0]), int(dopen[1]), int(dopen[2])).weekday()])
            print(("Request number " + str(rej[i]["number"]) + " was created on " + "{}").format(dopen))
        elif rej[i]["user"]["login"] == puller and rej[i]["state"] != "open":
            dopen = (rej[i]["created_at"].split("T")[0]).split("-")
            dopen = (calendar.day_name[datetime.date(int(dopen[0]), int(dopen[1]), int(dopen[2])).weekday()])
            dclose = (rej[i]["closed_at"].split("T")[0]).split("-")
            dclose = (calendar.day_name[datetime.date(int(dclose[0]), int(dclose[1]), int(dclose[2])).weekday()])
            print(("Request number " + str(rej[i]["number"]) + " was created on " + "{}").format(dclose) + " (already closed)")

if args.closeday:
    print("\n" + "Days of week when requests from " + puller + " were closed:")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller and rej[i]["state"] == "closed":
            dclose = (rej[i]["closed_at"].split("T")[0]).split("-")
            dclose = (calendar.day_name[datetime.date(int(dclose[0]), int(dclose[1]), int(dclose[2])).weekday()])
            print(("Request number " + str(rej[i]["number"]) + " was closed on " + "{}").format(dclose))

if args.deletions:
    print("\n" + "Number of deletions in requests from " + puller + ":")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller:
            delcount = requests.get((urlp + str({})).format(i), auth=authen)
            if delcount.json()["deletions"]:
                print("Request number " + str(rej[i]["number"]) + " contains " + str(delcount.json()["deletions"])+ " deletions")
            else:
                print("Request number " + str(rej[i]["number"]) + " has no deletions")

if args.additions:
    print("\n" + "Number of additions in requests from " + puller + ":")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller:
            addcount = requests.get((urlp + str({})).format(i), auth=authen)
            if addcount.json()["additions"]:
                print("Request number " + str(rej[i]["number"]) + " contains " + str(addcount.json()["additions"])+ " additions")
            else:
                print("Request number " + str(rej[i]["number"]) + " has no additions")

if args.number:
    print("\n" + "Number of comments in requests from " + puller + ":")
    for i in range(numpuls):
        if rej[i]["user"]["login"] == puller:
            comcount = requests.get((urlp + str({})).format(i), auth=authen)
            if comcount.json()["comments"]:
                print("Request number " + str(rej[i]["number"]) + " has " + str(comcount.json()["comments"])+ " comment(s)")
            else:
                print("Request number " + str(rej[i]["number"]) + " was not commented yet")
