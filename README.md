# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on poular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6

## Election-Audit Results
The analysis of the election show that:

- There were 369,711 votes cast in the election.
- The votes by county were:
  - Jefferson had 38,855 votes which was 10.5% of the total vote 
  - Denver had 306,055 votes which was 82.8% of the total vote
  - Arapahoe had 24,801 which was 6.7% of the total vote
- The county with the largest number of votes was Denver with 306,055 votes
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% and 85,213 number of votes
  - Diana DeGette received 73.8% and 272,892 number of votes
  - Raymon Anthony Doane received 3.1% and 11,606 number of votes
- The winner of the election was:
  - Diana Degette who received 73.8% of the vote and 272,892 number of vote

## Election-Audit Summary
The script provided is in a state that can be used for all future elections to calculate the winner of the popular vote.  However, in order to enhance the script in order for it to be used for an election, it may be necessary to make some slight modifications for the code.  One modification would be to have the code calculate the number of votes each candidate received in each county.  A nested 'for' loop would need to be created that would allow the script to pull out the 'candidate_votes' as it runs through each county, instead of the current setup which just pulls this data for the entire CSV file.  Another possible modification to ensure the accuracy of the election results, would be to create a script to make sure that every "Ballot ID" included in the CSV file was a unique ID number to ensure that no counts were double counted.  This could be created by establishing a boolean 'if' statement, to ensure that the number of unique ID numbers agrees to the 'total_votes' calculation.  Making these modifications to the script should help provide further insights to future election results as well as increase the confidence in the accuracy of those results.      
