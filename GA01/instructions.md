#To run the program, the following commands are provided:
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
