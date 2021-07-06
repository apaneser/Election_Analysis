# Election_Analysis

## Overview

### Purpose
The purpose of this project is to give additional information to Seth and Tom to complete the audit. They need the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout.

## Results
* The total amount of votes cast in this election was 369,711
  * Jefferson had 10.5% of the total votes at 38,855 votes 
  * Denver had 82.8% of the total votes at 306,055 votes
  * Arapahoe had 6.7& of the total votes at 24,801 votes
* The county with the largest amount of votes was Denver
* Diana DeGette won the election with 73.8% of the total votes at 272,892 votes

## Summary
This script can be used in any election as long as the csv file is formatted similarly. If the information needed are county and candidate votes, all that needs to be modified is the file path. Since the loops are built to handle any size of array and people, more counties and candidates can be added without changing the code at all. If the csv file isn't ordered the same, the row indexes may need to be modified. Some variables and strings can be modified to hold information for other locales like city or state instead of county. Much of the code can be recycled with  modification to add even more information like what percentage of candidates were voted from all the counties
