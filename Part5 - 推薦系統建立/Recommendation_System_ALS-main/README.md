# Recommendation_System_ALS
1. 在HDFS建立資料夾
* `$ hadoop fs -mkdir als`

2. 上傳資料到HDFS
* `$ hadoop fs -put ~/Desktop/als/rating_man.csv /user/spark/als`
* `$ hadoop fs -put ~/Desktop/als/outfit_man.csv /user/spark/als`
