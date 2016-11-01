#Test Case: 1

1. Objective
--------------------------

This Test Case will manually test all of the commands used in the weather function.

2. Command being tested:
------------------------------

  * hello: greeting
  * hi there: greeting
  * who are you: help function
  * what is your mission: help function
  * what can you do: help function
  * help me: help function
  * what's it like outside: current weather
  * what is the current weather: current weather
  * what are the current conditions: current weather
  * what is the weather like: current weather
  * what is the weather: current weather
  * what is the weather like: current weather
  * tell me the current weather: current weather
  * what's the weather right now: current weather
  * what's the weather supposed to be tomorrow: tomorrow's weather
  * what's tomorrows forecast: tomorrow's weather
  * what'll it be like tomorrow: tomorrow's weather
  * what is tomorrow's weather: tomorrow's weather

3. Expected output
--------------------------------
  * For a greeting we expect a random response from the following: "hi!", "hello there!!", or "what's up?"
  * For a help function we expect the following: I am CYBOT v00.03. I was programmed  to be totally obsessed with bus stops and weather! Try saying one of the following things to me:
    cybot, what's the weather
    cybot, when is the next basketball game
    cybot, what buses are coming to stop 1088
  * For current weather we expect the following: Right now in Ames, it is (current temperature) F and (condition). Today we see a high of (high temp), F and a low of (low temp). If it is a above 90 degrees we will get a random hot message, and if it is below 15 degrees you will get a cold message
  * For a tomorrow's weather function we expect the following: Tomorrow in Ames, we will see a high of (high temp) F and a low of (low) F (condition). If it is above 90 degrees, random hot message, if it is below 15 degrees, random cold message.

4. Observed output:
----------------------------
  * When prompted "hello", "hi", "hi there", and "helo"(to show fuzzy), cybot returned: "what's up" twice and  "hi!" twice
  * When prompted "who are you", "what is your mission", "what can you do", and "help me", cybot returned the help message every time.
  * when prompted with all of the various current weather commands cybot returned the current weather every time, which read "Right now in Ames, it is 60°F and Partly Cloudy. Today we'll see a high of 62°F and a low of 46°F." at 8:14 pm on Monday October 31st
  * when prompted with the several tomorrow's weather commands, cybot returned tomorrows forecast, which was: Tomorrow in Ames, we'll see a high of 72°F and a low of 50°F. Partly cloudy throughout the day.

5. The test is passed
------------------------------------

  10/31/2016:20:16
  Version: 00.03
