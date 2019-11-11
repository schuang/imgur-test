#!/bin/bash

for i in $(sqlite3 data.db 'select url from urls'); do
  wget $i -O images/`basename $i`
done
