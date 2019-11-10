#!/bin/bash
if [ -f data.db ]; then
   sqlite3 data.db -cmd ".headers on" -cmd ".mode column" "select * from urls"
fi
