#! /bin/sh
echo '----------------------------------------------------------'
date

set -ax

# maj de public_html sur idisk
#repIdisk=/Volumes/sbiner/Web/Sites
#rsync -avzu --stats --progress /Users/sbiner/Dropbox/Documents/site_web/public_html/* $repIdisk
#rsync -avzu --stats --progress maj_site.sh $repIdisk

# maj de public_html sur silenceisdefeat
 rsync -avzu -e ssh --stats --progress public_html/ sbiner@silenceisdefeat.com:/home/sbiner/public_html



