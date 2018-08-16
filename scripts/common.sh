#!/usr/bin/env bash

source "scripts/env.sh"

COLOR_BOLD_YELLOW="\033[1;33m"
COLOR_BOLD_BLUE="\033[1;34m"
COLOR_BOLD_MAGENTA="\033[1;35m"
COLOR_BOLD_CYAN="\033[1;36m"
COLOR_BOLD_RED="\033[1;31m"
COLOR_BOLD_WHITE="\e[1m"
COLOR_RESET="\033[m"


function fn_exists()
{
    type $1 | grep -q 'shell function'
}

function section {
    echo
    echo -e $COLOR_BOLD_MAGENTA$1 $COLOR_RESET
    echo "----------------------------------------------------------"
}

function warn {
    echo
    echo -e $COLOR_BOLD_RED"WARNING: "$COLOR_RESET$1
    echo
}

function finished {
    echo
    echo -e $COLOR_BOLD_WHITE"[DONE]"$COLOR_RESET
    echo
}

function info {
    echo
    echo -e "$COLOR_BOLD_CYAN$1 $COLOR_RESET"
    echo
}

function runtime {
    echo
    echo "----------------------------------------------------------"
    echo -e "=> $COLOR_BOLD_CYAN RUNTIME:$COLOR_RESET $COLOR_BOLD_WHITE$1$COLOR_RESET seconds"
    echo "----------------------------------------------------------"
    echo
}

function load_sql_dir {
    for target in $(ls $1)
    do
        echo "loading $1/$target"
        psql -f $1/$target
    done
}

# function render_rmd_dir {
#     for target in $(ls $1)
#     do
#         echo "rendering $target"
#         $SCRIPTS/renderRmd $1/$target $2
#     done
# }
#
# function render_reports {
#     for target in $(ls $REPORTS)
#     do
#         echo "rendering $target"
#         $SCRIPTS/renderRmd $REPORTS/$target $OUTPUT
#     done
# }



function clean_if_not_empty {
    if [ "$(ls -A $1)" ]; then
         echo "cleaning $1"
         rm $1/*
    else
        echo "."
    fi
}


function safelink {
    if [ ! -e  $2 ]; then
        sudo ln -s $1 $2
    else
        warn "$2 already exists"
    fi
}

function overlink {
    if [ ! -e  $2 ]; then
        sudo ln -s $1 $2
    else
        warn "$2 already exists, overwriting it"
        sudo rm $2
        sudo ln -s $1 $2
    fi
}

function ptestkill {
    pgrep -f $1 > /dev/null
    if [ $? -eq 0 ]; then
      warn "$1 process is running. killing it"
      pkill -9 -f $1
    else
      echo "."
    fi
}



# bash trick to get directory which contains the script
# SCRIPTS=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
# ROOT=$(dirname $SCRIPTS)
# DATA=$ROOT/data

# echo "ROOT: $ROOT"
# echo "SCRIPTS: $SCRIPTS"
# echo "DATA: $DATA"
