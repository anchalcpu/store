"""Top-level package for RP To-Do."""
# rptodo/__init__.py
import socket

__app_name__ = "store"
__version__ = "0.1.0"


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    ID_ERROR: "to-do id error",
}