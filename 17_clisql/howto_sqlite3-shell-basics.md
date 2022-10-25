# how-to :: USE BASIC SQLITE
---
## Overview
SQLITE is a good way to store data in databases. SQLITE will be useful in our talos problem and future projects, so it is good idea to learn it. Databases allow us to easily access big chunks of organized data.

### Estimated Time Cost: 0.8 Hours

### Prerequisites:

- Installed working version of `sqlite3` or `sqlite3.exe`
- There are resources below that detail how to intall sqlite on Mac, Windows, and Linux.

### Steps to Using SQLITE for Beginners:
0. The first step is to activate sqlite (similar to how we used python virtual environments): 
   - `$sqlite3`  -> activates the SQLITE terminal without a file
     - You can use `.OPEN <nameOfExistingFile>;` to open a sqlite file to edit or access
   - `$sqlite3 <nameOfNewFile>` -> activates it with a new file 
1. Now that are you in the sqlite terminal, you can start by creating tables: `create table <tableName>( <colName> <parameter>, <colName1> <parameter1>);`
   - Ex: `create table college(name TEXT, rate INTEGER);`
   - Parameter examples: 
     - INTEGER: Only integer values are allowed to be in the column
     - TEXT: Only text is allowed to be in the column
     - BLOB: Any type of data is allowed to be in the column
2. Now that you have created a table you will want to add data to the table obviously:
   - `insert into <tableName> VALUES(value0, value1);` -> Note you will need to have more parameters if your table has more columns
3. Now that you have added data, you want to be able to access it
   - `select * from <tableName>;` -> This command will return the whole table
   - `select <colName> from <tableName>;` -> This command will return a whole column from the table
4. Now that you have messed around with your sqlite file, you will want to save and exit. 
   - `.save <nameOfFile>.db;`
   - Press **Ctrl + D** to quit and **Ctrl + C** to force quit

### Extra Tips: 
- Additional options: `.header on` shows names of columns.
- `.tables` shows all tables
- `.mode column|csv|list|html|insert|line|tabs" shows different organizations of tables on use of "select ...`


### Resources
* [Link to Download sqlite3 on **MAC**](https://tableplus.com/blog/2018/08/download-install-sqlite-for-mac-osx-in-5-minutes.html)
* [Link to Download sqlite3 on **WINDOWS**](https://tableplus.com/blog/2018/08/download-install-sqlite-for-mac-osx-in-5-minutes.html)
* [Link to Download sqlite3 on **LINUX**](https://tableplus.com/blog/2018/08/download-install-sqlite-for-mac-osx-in-5-minutes.html)

---

Accurate as of (last update): 2022-10-25

#### Contributors:  
Yusha Aziz, pd 02 (Team Bottlers)  
Fang Chen, pd 02 (Team Bottlers)  
Jeff Chen, pd 02 (Team Bottlers)  
