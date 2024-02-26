#!/bin/bash
USERNAME=pi
SCRIPT="pwd; ls"

if [$# -eq 0]
then
    HOSTNAME="jigglypuff"
else
    HOSTNAME=$1
fi

ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
