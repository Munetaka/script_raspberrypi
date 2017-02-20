#!/bin/sh

    
video_list=`ls /dev/* | grep video`

check_video() {
    if [ -z "${video_list}" ]; then
        echo 'no video device'
        exit 1
    fi

    echo '=== video device list ==='
    for video in ${video_list}; do
        echo ${video}
    done
    echo '========================='
}


capture() {
    for video in ${video_list}; do
        echo "start: fswebcam -q -S 20 --no-banner -d ${video} tmp/`basename ${video}`_`date +%s`.jpg &"
        fswebcam -q -S 20 --no-banner -d ${video} tmp/`basename ${video}`_`date +%s`.jpg &
    done
    wait
    echo 'finish all'
}


check_video
capture

exit 0
