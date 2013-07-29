wsping
======

This project measures round-trip-time(RTT) (similarly to the 'ping' command) over a web socket. 
Server time-stamps are added to the timing packets to enable differential uplink/downlink delay measurement.

The back-end is implemented using tornado and the results are displayed in the browser using the flot chart library.

