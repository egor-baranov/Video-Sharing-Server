# Server-side for Video Sharing App

## What is it? 
This is an open repository of a server of app that allows you to record videos, share them, and also make video broadcasts.  
Now it is being hosted at https://kepler88d.pythonanywhere.com

## What has already been implemented
* Prototypes of base app functionality. 
* Data serialization. 
* Almost all working of the admin stuff. 

## What is going to be implemented soon
* Maybe db will be refactored to MongoDB.
* Some another functionality (etc SMS API).

# List of possible requests (server API description)

## App requests

### login
Request that is used to login user that is already been registered in system using phone or email as login and password. 
Parameter | Description
----------|-------
```phone``` | Phone number of user to login.
```email``` | Email of user to login.
```password``` | Password of logged-in user. 

### register
Parameter | Description
----------|-------
phone | Phone number of user to login.
email | Email of user to login.
password | Password of logged-in user. 

### list

### videoList

### userList  

### commentList

### addVideo
Request that is used to add video with passed data by user with selected login (phone or email).  
Very important thing is that videoId is generated on the user side.

Parameter | Description
----------|-------
phone | Phone number of user to login.
email | Email of user to login.
title | Title of video. 
descrirption | Description of video. 
tags | Array with tags of video (array of strings). 
size | Size of video in bytes (int). 
length | Length of video in seconds (int). 
videoId | Id of video (int). 

### getVideos

### getUploadedVideosStats

### getFavourite

### getUploadedVideos 

### addComment

### getComments

### getViewCount

### exist
Returns true if user with passed login (phone or email) exist else false. 

Parameter | Description
----------|-------
phone | Phone number of user.
email | Email of user.

### likeVideo

### videoLikeCount

### openVideo

## Admin requests

### blockUser
Parameter | Description
----------|-------
phone | Phone number of user to login.
email | Email of user to login.
password | Password of logged-in user. 

### resetPassword

### deleteComment

## Link to the app repository
https://github.com/egor-baranov/Video-Sharing-App
