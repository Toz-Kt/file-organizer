# file-organizer (Work in progress)
Python script that sorts files in a folder into subfolders by type

# File Organizer (v1)

Python script that sorts the files in a folder into subfolders by type.
It skips folders, temporary download files and files modified in the last 5 minutes.

Usage: set `start` (folder to sort) and `final` (where to move files), then run `python file_sorter.py`.

Status: v1, work in progress.

It never overwrites files: duplicates get a _1, _2 suffix.
It skips files that are in use instead of crashing.
