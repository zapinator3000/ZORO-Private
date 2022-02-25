# ZORO
## Zack's Open Row-Oriented Memory scheduler

This is the private repository with currently closed source code.

ZORO is an attempt to re-think how CPU's schedule memory transactions by grouping transactions that are in the same row into transaction groups.

BRANCHES:

Testing (From Linode)

Production (Jack's PC)

Production (Zack's PC)

## DRAMSIM3_mods

This file contains different configurations of ZORO, specifically the number of max retries

## Build Instructions

To build, get a copy of GEM5 from the website
Then, get a copy of DRAMsim3 from the DRAMsim3 GitHub repository
Be sure to build DRAMsim3 first
Also if installing ZORO, replace the files in this repository with the stock ones from GEM5
(Instructions are in ZOROmods)

## Compile Instructions

GEM5 with ZORO can be compiled using the script:

`` ./compile_gem5.sh ``

## Running GEM5 with ZORO
GEM5 with ZORO can be run using the script:

``./run_gem5.sh``

## Running an entire suite of different MAX_RETRIES values:
``python ./run_Series.py``
## Notes:

Be sure to place the scripts in GEM5's root directory first
