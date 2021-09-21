BUILD_ID=dontKillMe
ProcNumber=`ps -ef | grep -w python | grep -v grep | wc -l`
if [ $ProcNumber -el 0 ];then
    echo "Django is not run"
    nohup python3 manage.py runserver 0.0.0.0:8000 >django.log 2>&1 &
else
    kill -9 $(ps -ef |grep python | grep -v grep | awk '{print $2}')
    nohup python3 manage.py runserver 0.0.0.0:8000 >django.log 2>&1 &
    echo "Django is restarting...，"
fi
