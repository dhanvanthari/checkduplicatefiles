# checkduplicatefiles

## Build and run this image:
```
#############################
$ cd checkduplicatefiles
$ docker build -t python-checkduplicatefiles .
$ docker run -dit --rm --name "py-checkduplicatefiles" --hostname "py-checkduplicatefiles" -e DIRECTORY_NAME=testdir python-checkduplicatefiles
$ docker exec -it <containerID/ Name> /bin/bash
root@py-checkduplicatefiles:/app#python check_AllDuplicateFiles.py testdir
#############################
```
### OR

You can directly pull image from docker hub

`docker pull dhanvanthari/python-checkduplicatefiles`
