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

Registration of new user with selected parameters. 

Parameter | Description
----------|-------
```username``` | Username of new user.
```phone``` | Phone number of new user.
```password``` | Password of new user.  
```email``` | Email of new user.
```city``` | City of new user.
```birthDate``` | Birth date of new user,

### list

Returns all the data including list of all users and list of all videos (videoList + userList requests) with this format:
```
{
  "users": [
    // list of registered users data
  ], 
  "videos": [
    // list of uploaded videos data
  ]
}
```
This request does not require any parameters.

### videoList

Returns list of all videos with this format:
```
{
  "videos": [
    // list of uploaded videos data
  ]
}
```
This request does not require any parameters.

### userList  

Returns list of all users with this format:
```
{
  "users": [
    // list of registered users data
  ]
}
```
This request does not require any parameters.

### commentList

This request hasn't been implemented yet because comments needs refactoring to work with DatabaseWorker. 

### addVideo

Request that is used to add video with passed data by user with selected login (phone or email).  
Very important thing is that videoId is generated on the user side.

Parameter | Description
----------|-------
```phone``` | Phone number of user to login.
```email``` | Email of user to login.
```title``` | Title of video. 
```descrirption``` | Description of video. 
```tags``` | Array with tags of video (array of strings). 
```size``` | Size of video in bytes (int). 
```length``` | Length of video in seconds (int). 
```videoId``` | Id of video (int). 

### getVideos

Returns list of random videos serialized to JSON.
Parameter | Description
----------|-------
```phone``` | Phone number of user to login.
```email``` | Email of user to login.
```title``` | Title of video. 
```descrirption``` | Description of video. 
```tags``` | Array with tags of video (array of strings). 
```size``` | Size of video in bytes (int). 
```length``` | Length of video in seconds (int). 
```videoId``` | Id of video (int). 

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
```phone``` | Phone number of user.
```email``` | Email of user.

### likeVideo

### videoLikeCount

### openVideo

## Admin requests

### blockUser
Parameter | Description
----------|-------
```phone``` | Phone number of user to block.
```email``` | Email of user to block.

### resetPassword
Admin request that is used to reset password of user with selected login (phone or email).

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### deleteComment

## Link to the app repository
https://github.com/egor-baranov/Video-Sharing-App
