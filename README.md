# PCO
Python COmpressor - file archiver.
# To archive a file
Type: python3 pco.py >filename<

Or just run python3 pco.py and you will be asked for the file name in a following prompt.
# To extract a file
Type: python3 depco.py >filename<

Or just run python3 depco.py and you will be asked for the file name in a following prompt.
# Description
The PCO archiver in the current version uses simple functions that codes and decodes repeated sequences of data by one byte numbers. These numbers, followed by the sequences they describe, are then saved in the archive file in a process of compression. The archived file's name is the name of the original file with ".pco" added.
