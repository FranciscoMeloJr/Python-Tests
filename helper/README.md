
Helper Script
Helper functions to read/parse analyze log file.

Getting Started
1. Download
2. Run: python main.py -h

Prerequisites
-

Examples
python main.py -f=server.log -e    : enumarate the Exceptions 
python main.py -f=server.log -c  -v: display the caused by
python main.py -f=server.log -e -k : search on google
python main.py -f=server.log -e -w : enumarate and write to output.out the exceptions
python main.py -d -e -w: enumerate all exception in all the files in the directory, send to file output.out

Running the tests
  server.log - initial tests
  
Built With
Dropwizard - The web framework used
Maven - Dependency Management
ROME - Used to generate RSS Feeds

Versioning
 -
Authors
Francisco de Melo Jr.
Gabriel Alabarse Rocha Mendes  

License
This project is licensed under the MIT License - see the LICENSE.md file for details

Acknowledgments
 -
