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
  * If we use a bus stop number that is not recognized, or no buses within the next 15 minutes we expect CyBot to respond "No buses are arriving in the next 15 minutes for (stop number)""

4. Observed output:
----------------------------
  * Tested the four variations of next bus commands with the following stops, and got the following responses
    - Stop 1088: "Arriving at stop 1088 in the next 15 minutes: *2 Green West*  (Ontario/California): `bus #334` in 8min *3 Blue South*  (South 5th/South Duff): `bus #421` in 8min *23 Orange*  (Free Circulator/Iowa State Center to Beach Ave. at Sunset Dr.): `bus #975` in 2min *9 Plum*  (Campus): `bus #108` in 3min, `bus #108` in 1min"
    - 1193: "No buses are arriving in the next 15 minutes for stop 1193"
    - 1123: Arriving at stop 1123 in the next 15 minutes: *21 Cardinal*  (Free Circulator/Frederiksen Ct.): `bus #127` in 11min *3 Blue North*  (Mall via Schilletter): `bus #504` in 4min *6B Brown*  (Mall via Somerset to Stange Rd. at Aspen Rd.): `bus #429` in 9min *6A Towers*  (Towers/Campus): `bus #187` in 1min *2 Green East*  (Mall via Ames High School): `bus #1115` in 2min
    - 3923: No buses are arriving in the next 15 minutes for stop 3923

  5. The test is passed
  ------------------------------------

    10/31/2016:20:49
    Version: 00.03
