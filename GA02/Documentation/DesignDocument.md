# CyBot-Ultimate
### System Design Proposal
### Team Ultimate
### October 21, 2016

### Introduction:

This document will provide an overview of Team Ultimate's design for a Slack-based chat bot, CyBot-Ultimate. It will cover proposed functionality, bot format, development timeline, planned modules and components, and all external data sources that will be utilized.

### Proposed Functionality:

CyBot-Ultimate will have three major functions: bus data, current weather data, and Iowa State Football Schedule. Users will interact with the bot through a designated group Slack channel that the bot has been invited to, or through Slack private messages. Each of the three main external data features will be divided into modules. All chat messages to the bot in the group channel will be identified using a trigger word, CyBot. Messages in private chat will not require the trigger word.

### Development Plan:

Project development work will be split up among team members to allow for completion before the November 2nd deadline. Each member will work on one of the main modules of CyBot Ultimate.

### Dependencies:

#### Python v3.x
CyBot-Ultimate will run in a Python environment, meaning all dependencies will be Python-based.

#### Requests
CyBot will make use of the requests package to make requests to the various API's that will provide information to the bot's external data-driven packages. This package can be installed via PIP.

#### Python Slack Client
CyBot will make use of Slack's official Python Slack Client package for interfacing with Slack's servers. This module will be utilized for sending out chat responses, as well as for its Real Time Messaging functionality, which we will use to receive messages as the bot receives them.

#### Isolation of Dependencies
Virtualenv and PIP will be used to handle Python application dependencies.
Starterbot in virtualenv will isolate our application dependencies from other Python projects.
```
pip install virtualenv
Starterbot: virtualenv starterbot
Activate the virtualenv: source location of starterbot
```

### Planned Modules:

#### Main Bot Script
The main bot module will use the package of SlackClient to connect to the slack servers. This script will be the main interface between Slack users and all of the other modules in the bot.

#### Bus Information
The bus information module will get CyRide data from the NextBusXMLFeed API, parse the response and return the relevant data to the main program. The module will contain a function that takes a bus stop number as an argument and returns a list of the routes that service that particular stop, as well as a list of busses arriving in the next 15 minutes.

#### Weather Conditions
The Weather Conditions module will contain two major functions. One to return the current weather conditions, and one to return the forecasted weather conditions for the next day. This module will make use of the Dark Sky weather API.
The current conditions function will return the most recently collected snapshot of weather data for the Ames area. This snapshot will include current temp, forecasted high, forecasted low, as well as the current conditions.
The forecast function will return similar results, but instead of returning data for the current day's conditions, it will instead return data for the next day (tomorrow).

#### Iowa State Sports Schedule
This module will read the cyclones.com schedule RSS feed to determine upcoming ISU athletic events.  It will parse the RSS response and get the next couple of events that have not yet occurred.

### Data Sources:

#### Weather
For our weather function, we will reincorporate DarkSky API to get current and future forecasts. As we previously used DarkSky before and have clear understanding how to request weather information, we think using DarkSky again will work to our advantage.

#### Bus
We plan on using the NextBus API to gather information on next bus times. The information will also provide other bus routes that stop at the same bus stop, and times for the previous and next bus stop for the same route.

#### Sports
We plan to use the Cyclones.com calandar RSS feed to retrieve the titles and dates/times of upcoming ISU sports events.

### Functionality:

#### Main Bot:
In the Main Bot Script module, We will use the OS system to interact with the inputs that user puts. We will have a system that deals with two types of inputs, chatting inputs and technical inputs. Chatting input system will enable the Bot to be more human. For example, If user enters  “Hello” as an input, the module will ask the Bot to randomly return either “Hey”, “Hello” or “What’s up”.

Technical inputs will ask module to interact with Bus information module, Weather Condition module and also Iowa Sport Schedule Module. If user enters “-w T-D”, module will ask Bots to return Ames temperature from the day before in Fahrenheit. The beginning of each input will be the command to tell main module with module we are going to use. In this case, “-w” is the command for Weather Condition. Other than that, we have “-b” for Bus information and also “-s” for Sport Schedule Module.

Fuzzy Wuzzy package will be used to deal with the typos. If user types ”Hallo”, Fuzzy Wuzzy should be able to find the closest string in the module, which in this case is “Hello”. However, if the input that user enters is way off than the expected inputs in the module (if the distance number returned from Fuzzy Wuzzy package is bigger than our limit), we will print either “I don’t understand what you are saying. Please enter -h for help” or “It is not clear for me. Please enter -h for help”. For the help command, we will have “-h”, “-hw”, “-hs” and “-hb”. “-h” will return the general structure of the bot and how it works. “-hw”, “-hs” and “-hb” will specifically focus on how each technical module works.

#### Bus Information:
Using the NextBusXMLFeed API, a user will enter the bus stop number, which is used to indicate the location of where the bus will be stopping, and the Bus module will return the next busses that will be arriving at that location including their numbers. It is assumed that the user will get the bus stop number from the location they are trying to get the bus at, however, for testing purposes, we can provide a list of bus stops numbers. The command for this hasn’t been agreed upon as of yet however it will function similarly to help command.

To parse the XML document created from the NextBustXMLFeed API, the ElementTree package was imported. ElementTree is a standard package in Python 3.

#### Iowa State Sports Schedule:
Using cyclones.com calendar, we will provide the Iowa State athletics calendar of upcoming games to the user. A user will enter a sport that they want the calendar for, e.g. “basketball”, “baseball”, “gymnastics” etc. and the module will return when the next game will be and who it will be against. Other functionalities that might be added would be the location of that game.

#### Weather conditions:
The Weather conditions module will take the inputs from main bot. The data will be returned either current or historical data from DarkSky API depending on the inputs. Help section will also be provided.
### Task:
#### Matt Thompson:
Leader. Helper. Matt has the better understanding and skills of Python. Matt will lead the team to finish the code. Matt can interact any of the module. Matt will also be the helper to help the team members out.
#### Keng Hu:
Main Bot Script Builder. Keng is in charge of building out the main bot script to interact with other modules.
#### Liliane Iragena:
Bus Information Builder. Liliane will build up the Bus Information module to return bus schedule for different buses.
#### Woo Voong:
Sport Schedule builder. Woo will find RSS Feed to build the Sport Schedule module that will return the sport schedule depending on the the type of sport.
#### Lieb Chol:
Module tester. Lieb will test the Modules and record the result while he is testing.

#### Nate Burger:
Document person.
