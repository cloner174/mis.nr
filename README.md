# nr
Nothing so far!
$ git clone https://github.com/whitews/flowio

$ sudo apt update
$ sudo apt install python3-venv

$ python3 -m venv .nr


$ pwd #copy the show content

#this is your current path!
#if you see any space in it, you must use quotation whether single ' or double " before and after all the path below when you want use them. other wise you will get an error
#example of existence :: /home/admin/Doc MyDocuments/Python/ --->> I will use it like this:: "/home/admin/Doc MyDocuments/Python/"

#You will notice that any time you are at the main dicrectory of project, where the .nr folder is present, you do not need to use all the path to your enviremntal python !
#dont be disapointed if you can not understand the cause of it or even you do not have idea about that kind of stuff, you will figure all that out soon.

$ source 'pwd_results/.nr/bin/activate' #for example mine is::  $ source /home/admin/Documents/Python/mis.nr/.nr/bin/activate

$ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install --upgrade pip

$ cd flowio


$ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install .


# if you saw an error like this:: Missing dependencies for SOCKS support
#simply use the sudo command at the start of pip install lines


# mis.nr

If you do not have venv on your machine , use this for linux ( apt base disterbutions )::

        $ sudo apt update
        $ sudo apt install python3-venv

then;

        $ python3 -m venv .nr
to create a new private envirement for our project.

now do this::

        $ pwd     #-->>>  copy the shown content
This is your current path.
If you see any space in it, you must use quotation whether single ' or double " before and after all the path below when you want use them, Other wise you will get an error!
Example of existence an space! :: /home/admin/Doc MyDocuments/Python/ --->> I will use it like this:: "/home/admin/Doc MyDocuments/Python/"

to start working with your lcoal and new created envirement , in linux use ::

        $ source 'pwd_results/.nr/bin/activate'

You will notice that any time you are at the main dicrectory of project, where the .nr folder is present, you do not need to use all the path to your enviremntal python !
Do not be disapointed if you can not understand the cause of it or even you do not have idea about that kind of stuff, you will figure all that out soon.

        $ source 'pwd_results/.nr/bin/activate' 
        #for example mine is::
        $ source /home/admin/Documents/Python/mis.nr/.nr/bin/activate

Now upgrade pip using this command::

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install --upgrade pip


then;

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install flowcytometrytools

If you saw an error like this:: Missing dependencies for SOCKS support
Or even this:: pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPoo
Simply use the sudo command at the start of pip install lines::
        $ sudo /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install --upgrade pip
        $ sudo /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install flowcytometrytools
