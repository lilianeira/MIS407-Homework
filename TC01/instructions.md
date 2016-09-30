# Instruction for running AmesWeather simmulation
These are the instruction for running AmesWeather simulation. The program extracts weather data from openweathermap and provides a command line interface to the program so that it can be integrated into a large data collection system that MegaResearch Inc. are developing.

To run the program, the following commands are provided:
  * Measure: { P | T | WS | WD }
     * P = pressure
     * T = temperature
     * WS = wind speed
     * WD = wind direction
  * Time-offset: {Y | M | W | D}
      * Y = year
      * M = month
      * W = week
      * D = day

## Data Source Information
Using darksky.net api (formerly known as forecast.io) Using this as our data source for both our current and historical weather. The Dark Sky API uses a wide range of data sources, which are aggregated together to provide the most accurate forecast possible for a given location, including the NOAA NEXRAD system and the NOAA's Integrated Surface Database in the United States.
Please note this data source does not provide any information on the exact time that the data was collected, for this reason our program returns NA. Previous versions of this program returned the date and time that the API claimed their data represented, but the client requested that that data not be returned.

## Usage examples
To get the temperature for yesterday, last week, last year:

```$python AmesWeather.py T-D```

```$python AmesWeather.py T-W```

```$python AmesWeather.py T-Y```

To get the data for a specific date, specify the date in the format:
  * MM/DD/YYYY:HH:MM' where MM/DD/YYYY is the date, and HH::MM is * the time in 24hr

  * ```$python AmesWeather.py 6/10/2015:10:00 -M WS WS-M T T-M```
