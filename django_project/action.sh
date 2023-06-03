#! /bin/bash

OUTPUT=$(radon cc -a $1 | tee /dev/tty | tail -1)
#OUTPUT=$(radon cc -a $1 | tail -1)
# GRADE=$(echo $OUTPUT | grep -oP " \w " | tr -d '[:space:]')
# GRADE=C
rc=1

if [[ $GRADE == $2 || $GRADE < $2 ]] ; then  rc=0 ; fi

exit $rc