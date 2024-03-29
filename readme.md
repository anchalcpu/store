# store 

The system is a server-client based cli app build with python 3.8

## Getting started

* Kindly make sure you have Python v3.8.8 or above installed.

* Next thing to do is to clone the repository:

    ```
    $ git clone --branch=main https://github.com/anchalcpu/store.git
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
    For frequent words in all file:
    ```
    pythom -m store freqentwords -o dsc/asc
    ```
* Deploying in k8 cluster :

1. First make secret for pulling image .use command:
```
kubectl create secret docker-registry docker-credentials --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email> -n <your-namespace>
```
2. Apply all files in k8 folder.
