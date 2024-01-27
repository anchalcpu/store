from typing import List
import threading
import typer
from store import ERRORS, __app_name__, __version__  
from store import server
from store import client

app = typer.Typer()
c=client.client()
x=server.server()
@app.command()
def add(
    filenames: List[str] = typer.Argument(None),
) -> None:
    
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    
    c.uploadFiles(filenames)

@app.command()
def rm(filename: str=typer.Argument(None),)->None:
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    c.remove(filename)

@app.command()
def update(filename: str=typer.Argument(None),)->None:
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    c.accessfiles(filename)
    
@app.command()
def wc(filename: str=typer.Argument(None),)->None:
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    c.count(filename)

@app.command()
def ls()->None:
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    c.list()


@app.command()
def frequentwords(order:str=typer.Option("dsc",
"--order",
"-o",
help="Choose dsc for most  and asc for least frequent words."))->None:
    t_server = threading.Thread(target=x.starts, daemon=True).start()
    c.frequency(order)



def _version_callback(value: bool) -> None:
    return 
