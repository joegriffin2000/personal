#!/bin/bash

for FILE in *.; do
	if [[ -f FILE ]]; then
		WORD=$(wc -w $FILE)
		LINE=$(wc -l $FILE)
		echo $FILE ${LINE::${#FILE}*-1} ${WORD::${#FILE}*-1}
	fi
done
