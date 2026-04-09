# COP 4930 Project 2
## Liam Sharkey, lks24e

This is a weather tracking script currently set up to track weather at multiple points 
along -74 longitude. This could be useful for meteorologists who wish to track trends
along certain areas. I currently have it set up for -74 long because I'm not a
meteorologist and don't know what groupings of data they would find most helpful.

## API
This uses open meteo, documentation here: https://open-meteo.com/en/docs
I chose open meteo because It had a large variety of datapoints to choose from 
and an intuitive interface with which to work. The downside are that it uses
coordinates rather than city names or other more human friendly location markers,
and tends to provide a lot of data that isn't requested and requires filtering.

## Goals

Track weather at given locations
Easily change location and pattern of tracking
Allow for long term compilation of data


To run just use 'python pipeline.py' while in the src directory
If it's able to connect successfully you will get "Request successful" 3 times in the 
terminal. once for each of the 3 times it requests, otherwise you may get some form of 
error message.