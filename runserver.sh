#!/bin/bash

if [! -f  /etc/nginx/conf.d/dorm_nginx.conf ];then
sudo cp dorm_nginx.conf /et/nginx/conf.d/dorm_nginx.conf
fi

sudo /etc/init.d/nginx reload

uwsgi --ini dorm_uwsgi.ini