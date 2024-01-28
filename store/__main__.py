
from store import   __app_name__
from store import cli 

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()