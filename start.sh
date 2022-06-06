#!/bin/bash
#------------------------------------------------------------------------------
python scrape.py $1 && python download_multi.py
#Todo#

echo "Done"
