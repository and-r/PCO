# PCO
Python COmpressor - file archiver.

# Running
The scripts run at every operating system with Python 3.x installed. The first keyword that runs Python 3.x is *python3* or *py*.

# To archive a file
Type: *python3 pco.py <path_to_file>*

Or just run *python3 pco.py* and you will be asked for the file name in a following prompt.
# To extract a file
Type: *python3 depco.py <path_to_file>*

Or just run *python3 depco.py* and you will be asked for the file name in a following prompt.
# Description
The PCO archiver in the current version uses simple functions that codes and decodes repeated sequences of data by one byte numbers. These numbers, followed by the sequences they describe, are then written to the archive file in a process of compression. The archived file's name is the name of the original file with ".pco" added.
