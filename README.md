# Puzzle-Dragons

I love playing the game, however as the complexity of dungeons increases I don't always have the time to lookup what kind of conditions I can expect to encounter. And going in blind often leads to defeat and wasted stamina. As all good players know, having the right team setup, with appropriate awoken, active, and leader skills along with hp, attack, and rcu often can push the success rate when tackling difficult dungeons in their favor.<br><br> This projects goal is to bypass the lookup of dungeon encounters and skip ahead to the strategy. The current stage of this project is in collecting and organizing the information on the dungeon encounters and on the monsters that will make up a players monster-box. <b>Project Steps Include:</b>

-   [x] Get Monster Profile and Abilities (active, awoken, leader skills)
-   [ ] Get Monster Stats such as ATK, HP, RCV
-   [x] Store Monsters in a Monster Box
-   [ ] Group Monsters into Teams
-   [ ] Calculate the ATK, HP, RCV, of teams
-   [ ] Calculate when Skills can be Activated
-   [x] Get Dungeon Information (stamina, battles, name, floors)
-   [x] Get Dungeon Encounters (floor number, monster name, atk, defence, skills)
-   [ ] Determine Method for Creating Strategy from this Information
-   [ ] Return Appropriate Team to Complete Dungeon

## Methodology

I believe that incorporating a machine learning model may be the most appropriate way to determine if teams can complete dungeons. Initial issues with training models is that they take a long time to train and each dungeon is very unique hence a unique training may be required for each attempted dungeon. A long time to get a winning strategy defeats the purpose of skipping the dungeon lookups. So until I can determine a better strategy I will be relying on teams skills and stats to determine the strategies that could win. For example, if Team Attack is higher than all the dungeon encounters HP + Defence then it may be a winning strategy. I expect the actual method for determining strategy success to be more complex than this. <br><br> As of right now I am collecting all the information that I think I may need in order to make any kind of strategy. Because PAD does not have an official API to collect this information, I have relied on their unofficial website <a href="http://www.puzzledragonx.com/en/monster.asp?n=6128">PuzzleDragonX</a> for all the information and have scraped in order to organize the data. Of course all credit goes to Gungho and the website.

## Files

Content Folder contains the web scraping functions using BS4. Player folder contains the Monster-Box. dungeons.py and monsters.py files instantiate the requests for relvant data.
<br><br>

This repo is still being worked on, but any assistance if anyone is reading this is appreciated.
