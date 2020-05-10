# deploying-web-app-on-docker
The app is build using python,flask and mysql.
Flask's request option is used to check against the methods like post and get to perform operations.
pymysql module is used to perform queries on the table by creating and then connecting to the database.

Instructions to dockerize the app:-
Keep all the above files and folder inside one root folder(except readme and postman collection).
cd to the root folder. 
Login as root user.
Run docker build command to create docker image from the docker file.
Then run the command docker run -p 127.0.0.1:8080:8080  <Image_Name>.
Now the app will run on http://127.0.0.1:8080/user .
Go to the above address in browser and do crud operations.
Crud operations can also be done using postman.(See devs.postman_collection.json file).
