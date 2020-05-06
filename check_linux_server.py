import subprocess
import os
import subprocess
import requests

def is_service_running(name):
    with open(os.devnull, 'wb') as hide_output:
        exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
        return exit_code == 0

class Slack:
    def __init__(self,report):
        webhook = 'https://hooks.slack.com/services/T92JCJW59/B012Qxxxxxxxxxxxxxxxxxxxxxxx'
        response = requests.post(webhook, json=report, headers={'Content-Type': 'application/json'})
        if response.ok:
            json_data = response.text
            self.result = json_data

if __name__ == '__main__':
    if not is_service_running('mysqld'):
        print ('mysql is not running')
        os.system("systemctl restart mysqld")
        result_dict = ("*MICHELONE SLACK* \n*MYSQL DOWN IM GOING TO RESTART* ")
        slack_report = {"attachments": [{"fallback": "*MICHELONE SLACK*", "color": "#FF0000", "text": result_dict}]}
        slack_push_log = Slack(slack_report)
    else:
        print("ALL OK")
    if not is_service_running('httpd'):
        print('httpd is not running')
        os.system("systemctl restart httpd")
        result_dict = ("*MICHELONE SLACK* \n*APACHE DOWN IM GOING TO RESTART* ")
        slack_report = {"attachments": [{"fallback": "*MICHELONE SLACK*", "color": "#FF0000", "text": result_dict}]}
        slack_push_log = Slack(slack_report)

    else:
        print("ALL OK")



