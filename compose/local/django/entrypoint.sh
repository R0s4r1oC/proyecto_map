#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

cmd="$@"

# N.B. If only .env files supported variable expansion...
if [ -z "${MYSQL_USER}" ]; then
   base_postgres_image_default_user='root'
   export MYSQL_USER="${base_postgres_image_default_user}"
fi
export DATABASE_URL="mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@mysql:33060/${MYSQL_DATABASE}"

mysql_ready() {
python << END
import sys

import MySQLdb as mdb

try:
   mdb.connect(
       db="${MYSQL_DATABASE}",
       user="${MYSQL_USER}",
       passwd="${MYSQL_PASSWORD}",
       host="mysql"
   )
except mdb.Error:
   sys.exit(-1)
sys.exit(0)

END
}

until mysql_ready; do
 >&2 echo 'MySQL is unavailable (sleeping)...'
 sleep 1
done

>&2 echo 'MySQL is up - continuing...'

exec $cmd
