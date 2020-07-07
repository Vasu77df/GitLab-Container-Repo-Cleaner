# Commands to setup the Gitlab Container registry deletor program as Scheduled job

## For Linux: Setting up a cron job
 
 - The deletor program would require python3 to installed if not avaiable, this can be done by running the following command in the terminal

#### For Debian based systems
 ```console 
 root@user:~$ sudo apt-get install python3
 ```

#### For Centos based systems 
```console 
root@user:~$ sudo yum install python3
```
- After installation copy the all files into found in the 

 0 9 * * * /bin/python3 /path/to/deletor.py