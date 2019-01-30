# CAPP Development Module
[![Build Status](https://travis-ci.org/justincohler/capp_demo.svg?branch=master)](https://travis-ci.org/justincohler/capp_demo)

[Accompanying Slide Deck](https://docs.google.com/presentation/d/1Y7EJ8do0qUN05D7yQeSgReTaOUcA7bIBS4b_ZWVNtmo/edit?usp=sharing)

**Purpose**: This repository serves to help CAPP students refresh their skills with unix-style command line tools, file-system, and common python development setup requirements for collaborative development.

## Speed up your workflow
Before we get started, there are five basic CLI tips that will make the rest of the module and your life easier:

1. Tab-to-complete: the ```tab``` key will auto-complete (case-sentive) file/folder names after the first letter entered. When traversing directories, or typing long filenames, use ```tabs```.
1. ```ctrl-a``` (beginning-of-line) and ```ctrl-e``` (end-of-line)
1. Tilde (```~```): represents your home directory
1. Wildcards (```*```): Looking for a file in your directory that starts with the letter 'B' or ends with "txt"? ```ls B*``` or ```ls *.txt``` to the rescue.
2. Last command (```!!```): the text of the last command. Example below:
    ```
    $> run /restricted_folder/restricted_file.py
    ERROR: Permission Denied
    $> sudo !!
    sudo run /restricted_folder/restricted_file.py
    ...
    ...
    Hello World!
    $>
    ```

**Note** - If you're curious about the details of any command going forward, use ```man <command_name>```, which brings up the linux (man)ual for that command.

***********************************************************
## Review Getting Around (Warmup)
### Cheatsheet

|     Command | Name                      | Description                              | Common arguments                                                 | Example                            |
| ----------: | :------------------------ | :--------------------------------------- | ---------------------------------------------------------------- | ---------------------------------- |
|    ```ls``` | List                      | list the contents of a directory         | ```<path>```, -a (all files, including hidden), -l (list format) | ```ls -al ~/```                    |
|   ```pwd``` | Present Working Directory | print complete path to terminal location |                                                                  | ```pwd```                          |
|    ```cd``` | Change Directory          | change terminal location                 | ```<path>```                                                     | ```cd /tmp/```                     |
|    ```cp``` | Copy                      | copy file/folder to location             | -r (recursively, for folders), ```<source>```, ```<dest>```      | ```cp -R my_folder /tmp/```        |
|    ```mv``` | Move/Rename               | move/rename a file/folder to location    | ```<source>```, ```<dest>```                                     | ```mv old_name.txt new_name.txt``` |
|    ```rm``` | Remove                    | remove a file/folder                     | -r (recursively), -f (force)                                     | ```rm -rf /tmp/my_folder```        |
| ```mkdir``` | Make Directory            | create folder(s)                         |                                                                  | ```mkdir dir1 /tmp/dir2```         |

### Exercise
* Run the following command to create an empty file named "one" in your user directory:
  ```
  touch ~/one
  ```
* Rename the file "two".
* Move it to the ```/tmp``` directory.
* Make a dirctory in ```/tmp``` called "test".
* Make a copy of the file in ```/tmp/test``` called "three" so that you have ```two``` in ```/tmp``` and ```three``` in your ```/tmp/test``` folder.
* Remove ```two``` from ```/tmp```.


***********************************************************
## Common Functions
piping
dumping (carrots)
con(cat)enate
head/tail
touch
grep
(p)rocess(s)earch 
kill

***********************************************************
## Working with Paths
Exporting a variable
Exporting PATH
/tmp, /opt, /usr/local
bashrc, bash_profile

***********************************************************
## Remote Shells (SSH)

SSH is a trust-based remote access system, one of the underlying ways of provisioning Amazon Web Services (AWS) and other cloud providers.

### Requirements
* a "public key" that can be shared with anyone (named ```id_rsa.pub``` by default)
* a "private key", never to be shared (named ```id_rsa``` by default)
* the public key stored in the host's ```authorized_keys``` file access to that host

### Why public and private keys?
When two users communicate over the internet, it is assumed that bad actors may listen to the wire communications. By combining your private key with another user's public key using clever elements of polynomials, you can establish trust via a confirmation message only the two users can decipher.

### Public and Private Keys
By default, keys live in ```~/.ssh```. If there are no keys in your user ssh folder, create keys via the following command-line program and follow the wizard (note that a password is not required):
```
$> ssh keygen
```
The above script will place a public and private "key pair" in your user's home directory (```~/.ssh```).

***********************************************************
### The ```config``` File
Creating ssh shortcuts for common locations can be done in the ```~/.ssh/config``` file, searched for by default by the ssh program. The basic format is shown below:
```
Host <nickname>
    User <username>
    Hostname <hostname>
```
There are plenty of other arguments, but for the sake of this exercise, these are all we need. 

### Exercise

* Paste the contents of your public key in the ```#capp-dev-module``` Slack channel.
* Create a new entry in your ```~/.ssh/config``` file (or a new file altogether) with the following details:
  * nickname: "capp-dev"
  * username: "ec2-user"
  * hostname: #TODO
* ssh into this host with ```ssh <nickname>```, in this case ```ssh capp-dev```. (Note this will only work once I've added your public key to the list of ```authorized_keys```)
* Create a new empty file with ```touch``` in the ec2-user's home directory.

***********************************************************
## Sending Files (SCP)
Send a file

***********************************************************
## Working with APIs
Curl
Download an http page
Post a message to a simple flask app

***********************************************************
## Python Mini-Environments
Conda, virtualenv
Conda create
Tradeoffs vs virtualenv

***********************************************************
## Further Virtualization (If we have Time)
Vagrant
Reduce lag, 
Repo-specific configuration

