# How can i make the python program to check linux services

I want to make simple python script , which i can run on cron job. 

i just want to see if these services are currently running or stopped

```
Httpd
mysql
```
so i create this script that check if MySQL and apache runs and in case are down it makes restart of the process and send SLACK message.

# CRONTAB

```
* * * * * root /usr/bin/python3 /home/michelone/check_status.py

```

# SLACK NOTIFICATION

![SLACK NOT](slack_not.png)
