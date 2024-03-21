# mis.nr

# requirements
bokeh==2.4.3
FlowIO==1.1.1
FlowKit==1.0.1
FlowUtils==1.1.0b0
ipython==8.22.2
pandas==1.5.3
seaborn==0.11.2

# additional!
ipykernel==6.29.3
jupyter_client==8.6.1
jupyter_core==5.7.2
keyring==24.3.1

If you do not have venv on your machine , use this for linux ( apt base disterbutions )::

        $ sudo apt update
        $ sudo apt install python3-venv


To create a new private envirement for our project:
        
        $ python3 -m venv .nr

now do this::

        $ pwd     #-->>>  copy the shown content
This is your current path.

If you see any space in it, you must use quotation whether single ' or double " before and after all of the path below when you want use them, Other wise you will get an error!
Example of existence an space! :: /home/admin/My Documents/Python/ --->> I will use it like this:: "/home/admin/My Documents/Python/"

to start working with your lcoal and new created envirement , in linux use ::

        $ source 'pwd_results/.nr/bin/activate'

You will notice that any time you are at the main dicrectory of project, where the .nr folder is present, you do not need to use all the path to your enviremntal python !
Do not be disapointed if you can not understand the cause of it or even you do not have idea about that kind of stuff, you will figure all that out soon.

        $ source 'pwd_results/.nr/bin/activate' 
        #for example mine is::
        
        $ source /home/admin/Documents/Python/mis.nr/.nr/bin/activate

Now upgrade pip using this command::

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install --upgrade pip

And;

        $ git clone https://github.com/whitews/flowio

        $ sudo apt update
        $ sudo apt install python3-venv

        $ python3 -m venv .nr


        $ pwd #copy the show content

#this is your current path!

        $ source 'pwd_results/.nr/bin/activate' #for example mine is::  $ source /home/admin/Documents/Python/mis.nr/.nr/bin/activate

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install --upgrade pip

        $ cd flowio

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python -m pip install .

If you saw an error like this:: Missing dependencies for SOCKS support
#simply use the sudo command at the start of pip install lines

        $ cd ..

        $ !git clone https://github.com/whitews/flowutils

        $ cd flowutils

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python3 setup.py install

        $ cd ..

        $ git clone https://github.com/whitews/flowkit

        $ cd flowkit

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python3 -m pip install -r requirements.txt

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python3 setup.py install

        $ /home/admin/Documents/Python/mis.nr/.nr/bin/python3 -m pip install IPython
