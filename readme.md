# store 

The system is a server-client based cli app build with python 3.8

## Getting started

* Kindly make sure you have Python v3.8.8 or above installed.

* Next thing to do is to clone the repository:

    ```
    $ git clone --branch=main 
    ```
    ```
    $ cd store 
    ```
* Create a virtual environment to install dependencies in and activate it:

    ```
    $ python -m venv .venv
    ```
    **OR**
    ```
    $ python3 -m venv .venv
    ```
    Activate the environment:
    ```
    $ .\.venv\Scripts\activate
    ```
    **OR**
    ```
    $ source .venv/bin/activate
    ```

* Then install the dependencies:
    ```
    (.venv)$ pip install -r requirements.txt
    ```
    **OR**
    ```
    (.venv)$ pip3 install -r requirements.txt
    ```

* Run below command for app info 

python -m store --help

* Excute below commands for required operations 

   For uploading files:
    ```
    python -m store add <filename1> <filename2>
    ```
   For update file:
    ```
    python -m store update <filename>
    ```
   For listing all saved files:
    ```
    python -m store ls
    ```

   For removing any file :
    ```
    python -m store rm <filename>
    ```
   For total number of words in any file:
    ```
    python -m store wc <filename>
    ```

