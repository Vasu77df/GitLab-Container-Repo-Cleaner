# Setup of the Gitlab Container registry deletor program as Scheduled job

## For Windows : Setting up task schedular
 - The deletor program would require python3 to installed if not avaiable in the system. 

 
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

 - This command runs the Container Registry Cleaner Program every day at 9 am. 

 - You can edit this using the reference below 

 ![cron_cmd_image](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/cron_cmd_image.png)

 - The program can also be manually run by navigating to the folder of the program directory and entering the command.

 ```console
root@user:~$ python3 deletor.py
```

**The default configuration is to delete all Image tags in the Contaner registry that are older than 1 day but 5 images will be retained from deletion.**

---

 ### Editing *credentials.json* file for specific user and different filters

- The contents of the credential.json file can be seen below

```json
{
    "User ID": 6336446,
    "Access-Token": "eXUd7tXUx6_gyEauXZ78",
    "Project ID": "19708510",
    "Registry ID": "1197041",
    "name_regex_delete": ".*", 
    "keep_n": 5,
    "older_than": "1d",
    "name_regex_keep": ".*"
}
```

- This file need to be edited according to the users accessability. 

- *User ID* can be found in [gitlab.com/profile](gitlab.com/profile) after you login. 

- A personal *access token* has to requested to access the Gitlab Container Registry API that the deletor program uses. 

![access_token](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/access-token.png)

- The *Project ID* can be found at the home page of every project.

- The *Registry ID* is the ID for for the registry that you would like to delete image tags in. It can be found be entering the following command on your terminal or powershell.

``` console 
root@user:~$ curl --header "Private-Token: your-access-token" "https://gitlab.com/api/v4/projects/project_id:/registry/repositories" | python3 -m json.tool

```

- You an also find out the registry ID by running the regID_finder.py program using the command 

``` console 
root@user:~$ python3 regID_finder.py
```

- The other parameters you can see are various filters that are used to delete container image tags according to certain rules. 

![api_filter](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/api_filter.png)

## 