## logs

# logs types

# General Query Log.
# Slow Query Log.
# Error Log.

SET GLOBAL log_output = "FILE"; # "Table"
SET GLOBAL general_log = 'ON';
   
SHOW VARIABLES LIKE '%file%';
SHOW VARIABLES LIKE '%dir%';

SELECT @@general_log;
SELECT @@general_log_file;

# MySQL version > 5 # set at runtime
SET GLOBAL log_output = "FILE"; # "Table"
SET GLOBAL general_log = 'OFF';
SET GLOBAL general_log_file = "/opt/homebrew/var/mysql/danish.log";
SET GLOBAL general_log = 'ON';

show full processlist;
kill 20;