#!/usr/bin/bash
#

function bot_running() {
    ps -ef|grep -v grep |grep "python3 Bot.py"
    return $?
}

function start_bot() {
    if bot_running; then
        echo "Bot has already been running. exit..."
    else
        echo "Starting bot..."
        source ~/bin/activate
        python3 Bot.py 1>Bot.log 2>&1 &
        echo "Bot started..."
    fi
}

function stop_bot() {
    while bot_running
    do
        ps -ef|grep -v grep |grep Bot.py | awk '{print $2}' | xargs kill -15
        echo "Kill signal sent. Wating for bot to exit...."
        date
        echo
        sleep 5
    done
    echo "Bot stopped..."
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
