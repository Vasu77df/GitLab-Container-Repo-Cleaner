# Setup of the Gitlab Container registry cleaner program as Scheduled job

## For Windows : Setting up task schedular
 - The cleaner program would require python3 to installed if not avaiable in the system. It can be downloaded and installed [here](https://www.python.org/downloads/). 

 - The dependency libraries have to then be installed. This is done by opening Powershell navigating to the program folder and installing the requriments by using the following command. 

 ```powershell
 C:\Users> SET-LOCATION \path\to\program
 C:\Users> pip install -r requirements.txt
 ```

 - Download the program from [here](https://gitlab.com/vasu3797/gitlab-image-repo-cleaner) and extract all contents of the files in your desired directory. 

 - Search for Task Schedular in the Start Menu and follow the steps seen below

 ![task_start](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/task_start.png)

![task_schedule](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/task_schedule.png)

![task_time](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/task_date.png)

- The command for the arguments field can be found bellow:

```powershell
C:\Users> python /path/to/program/cleaner.py
```
![task_action](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/task_cmd.png)


## For Linux: Setting up a cron job
 
 - The cleaner program would require python3 to installed if not avaiable, this can be done by running the following command in the terminal

#### For Debian based systems
 ```console 
 root@user:~$ sudo apt-get install python3
 ```

#### For Centos based systems 
```console 
root@user:~$ sudo yum install python3
```
- After installation copy or clone all the files of the program found in the repsitory [here](https://gitlab.com/vasu3797/gitlab-image-repo-cleaner) or by using the command 

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
 0 9 * * * /bin/python3 /path/to/cleaner.py
 ```

 - This command runs the Container Registry Cleaner Program every day at 9 am. 

 - You can edit this using the reference below 

 ![cron_cmd_image](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/cron_cmd_image.png)

 - The program can also be manually run by navigating to the folder of the program directory and entering the command.

 ```console
root@user:~$ python3 cleaner.py
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

- A personal *access token* has to requested to access the Gitlab Container Registry API that the cleaner program uses. 

![access_token](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/access-token.png)

- The *Project ID* can be found at the home page of every project.

- The *Registry ID* is the ID for for the registry that you would like to delete image tags in. It can be found be entering the following command on your terminal or cleaner.

``` console 
root@user:~$ curl --header "Private-Token: your-access-token" "https://gitlab.com/api/v4/projects/project_id:/registry/repositories" | python3 -m json.tool

```

- You an also find out the registry ID by running the regID_finder.py program using the command 

``` console 
root@user:~$ python3 regID_finder.py
```

- The other parameters you can see are various filters that are used to delete container image tags according to certain rules. 

![api_filter](https://github.com/Vasu77df/GitLab-Container-Repo-Cleaner/blob/master/images/api_filter.png)

## Garbage Collection to free up Disk Space
---

- To free up disk space in a you Gitlab Server the following command has to be run on the server. 

```console 
root@user:~$ sudo /opt/gitlab/embedded/bin/registry garbage-collect -m /var/opt/gitlab/registry/config.yml
```

This command will delete all layers that are unreferenceed by the tags and without manifests 

- To set this command as a cron job in your Gitlab server to run everyday at 9 pm. 

```console
 0 21 * * * sudo /opt/gitlab/embedded/bin/registry garbage-collect -m /var/opt/gitlab/registry/config.yml
```

**Running this command will stop the Container Registry and users will not be able to access them causing a downtime**

### Performing garbage collection without downtime
---

You can perform a garbage collection without stopping the Container Registry by setting it into a read-only mode and by not using the built-in command. During this time, you will be able to pull from the Container Registry, but you will not be able to push.

To enable the read-only mode:

- In /etc/gitlab/gitlab.rb, specify the read-only mode:

```json
  registry['storage'] = {
    'filesystem' => {
      'rootdirectory' => "<your_registry_storage_path>"
    },
    'maintenance' => {
      'readonly' => {
        'enabled' => true
      }
    }
  }
```

- Save and reconfigure GitLab:

```console
sudo gitlab-ctl reconfigure
```

- sudo gitlab-ctl reconfigure

```console 
sudo /opt/gitlab/embedded/bin/registry garbage-collect -m /var/opt/gitlab/registry/config.yml
```

Follow this [link](https://docs.gitlab.com/ee/administration/packages/container_registry.html#container-registry-garbage-collection) for more reference about garbage collection. 
---