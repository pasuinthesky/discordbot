#!/usr/bin/bash
#

function start_bot() {
    source ~/bin/activate
    python3 Bot.py 1>Bot.log 2>&1 &
}

function stop_bot() {
    while ps -ef|grep -v grep |grep "python3 Bot.py"
    do
        ps -ef|grep -v grep |grep Bot.py | xargs kill -15
        echo "Kill signal sent. Wating for Bot to exit...."
        date
        echo
        sleep 5
    done
}

case "$1" in
start)
    start_bot
    ;;
stop)
    stop_bot
    ;;
restart)
    stop_bot
    start_bot
    ;;
*)
    echo "Usage: botctl [start|stop|restart]"
esac
    