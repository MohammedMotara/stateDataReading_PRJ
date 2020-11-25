# stateDataReading_PRJ
This is a repo of work completed for my state data reading project using Python.

In order to get this project to work, please do the following

1. delete the census2020.py file, this has only been uploaded to evidence that the initial py script works.
2. Run the readCensusExcel sheet
3. Using your interactive shell navigate to the working direction of the newly created census2020.py file
4. run the following commands.
```
>>> import os
>>> import census2010
>>> anchoragePop = census2020.allData['AK']['Anchorage']['pop']
>>> print('The 2010 population of Anchorage was ' + str(anchoragePop))
```
The population should be 291826.
