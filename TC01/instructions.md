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

## Usage examples

To get the temperature for yesterday, last week, last year:

```$python AmesWeather.py T-D```

```$python AmesWeather.py T-W```

```$python AmesWeather.py T-Y```

To get the data for a specific date, specify the date in the format:
  * MM/DD/YYYY:HH:MM' where MM/DD/YYYY is the date, and HH::MM is * the time in 24hr

  * ```$python AmesWeather.py 6/10/2015:10:00 -M WS WS-M T T-M```
