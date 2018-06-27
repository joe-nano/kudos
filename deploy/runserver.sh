#!/bin/bash
export PATH=/home/leswing/anaconda3/envs/kudos/bin:/home/leswing/anaconda3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd src/kudos
gunicorn kudos.wsgi -b 0.0.0.0:8000
