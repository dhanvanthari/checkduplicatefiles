# checkduplicatefiles

<h2>Build and run this image:</h2>

$ cd checkduplicatefiles
$ docker build -t python-checkduplicatefiles .
$ docker run -dit --rm --name "py-checkduplicatefiles" --hostname "py-checkduplicatefiles" -e DIRECTORY_NAME=testdir python-checkduplicatefiles
$ docker exec -it <containerID/ Name> /bin/bash
root@py-checkduplicatefiles:/app#python check_AllDuplicateFiles.py testdir
