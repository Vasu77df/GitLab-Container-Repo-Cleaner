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
- After installation copy or clone all the files found in the repsitory [here](https://gitlab.com/vasu3797/gitlab-image-repo-cleaner) or by using the command 

```console
root@user:~$ git clone https://gitlab.com/vasu3797/gitlab-image-repo-cleaner.git
```
- Save this file to your desired directory

- To setup a cron job you would require to enter the following command and append the file 

```console
root@user:~$ crontab -e 
```

- you will see the following file:

![crontab_image](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/crontab_image.png)

- Enter the command seen in the image or in the you can see below

```bash
 0 9 * * * /bin/python3 /path/to/deletor.py
 ```