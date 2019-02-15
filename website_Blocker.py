import time
from datetime import datetime as dt


hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["https://www.facebook.com","www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]
list = input("Enter the website you want to block:")
if list in website_list:
    print("Checking Block list...\n")
    time.sleep(2)
    print( "Already exist...\n")

else:
    print("Checking Block list...")
    website_list.append(list)
    time.sleep(2)
    print("Adding to Site Blocking list...")

starting_time = int(input("Starting time:"))

end_time = int(input("End time:"))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,starting_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website + "\n")

    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
