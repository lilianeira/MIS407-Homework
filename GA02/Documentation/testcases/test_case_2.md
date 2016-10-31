#Test Case: 1

1. Objective
--------------------------

This Test Case will manually test all of the commands used in the bus function.

2. Command being tested:
------------------------------

  * I'm at stop (stop number): next bus response
  * I am at bus stop (stop number): next bus response
  * what busses are coming to stop (stop number): next bus response
  * What busses can I expect at stop (stop num): next bus response

3. Expected output
--------------------------------
* For all of the above commands we expect that CyBot will return all of the busses for each stop that wil be coming in the next 15 minutes. We expect route number, route color, bus number, and how many minutes until it is arrived at the requested stop.
* If we use a bus stop number that is not recognized we expect CyBot to respond "I do not know anything about stop: (stop number)"

4. Observed output:
----------------------------
