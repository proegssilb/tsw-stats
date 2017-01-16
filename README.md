# tsw-stats
While [Advanced Combat Tracker](http://advancedcombattracker.com/) is excellent at capturing data, it could use some work in how
it lets people explore that data.

This project will, once it is actually vaguely ready for use, let people poke around encounters, and see how well their character
did in combat. The expected flow is to have TSW generate combat logs, then parse those logs with ACT (and have ACT automatically
export to SQL), and then view the parse results with tsw-stats.

For now, the software isn't even really ready for github, but it's going to be a while before v0.1 is ready. So, I've posted a 
[Python](https://www.python.org/)/[SqlAlchemy](http://www.sqlalchemy.org/)-based data model to allow writing software on top of 
ACT's SQL export of TSW data.
