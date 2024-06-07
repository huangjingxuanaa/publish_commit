if [ ! $1 ]; then  
   echo 'ERROR: Need to apply loop param'    
   exit  
fi  
for i in $(seq 1 $1)
do 
   `sh ./push.sh`
   time=`date +'%G-%m-%d %H:%M:%S' -d '-1 days'`
   timedatectl set-time "2021-09-10 20:44:22"
done


