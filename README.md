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

# Project architecture
```
│   main.py
│   README.md
│   requirements.txt
│
├───components
│   │   config.py
│   │   core.py
│   │
│   ├───database
│   │   │   DatabaseWorker.py
│   │   │
│   │   └───data
│   │           blocked_users.json
│   │           comments.json
│   │           users.json
│   │           videos.json
│   │    
│   └───managers
│           CommentManager.py
│           UserManager.py
│           VideoManager.py
│
├───dto
│       Comment.py
│       User.py
│       Video.py
│    
├───lib
│       smsc_api.py
│
├───routes
│   ├───admin_panel
│   │       admin_requests.py
│   │       user_editing.py
│   │
│   └───app_requests
│           data_list.py
│           regular_requests.py
│       
└───tests
        test_dbworker.py
```

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
    // list of uploaded videos 
  ]
}
```
This request does not require any parameters.

### videoList

Returns list of all videos with this format:
```
{
  "videos": [
    // list of uploaded videos 
  ]
}
```
This request does not require any parameters.

### promotionalVideoList

Returns list of promotional videos with this format:
```
{
  "promotionalVideos": [
    // list of promotional videos 
  ]
}
```
This request does not require any parameters.

### userList  

Returns list of all users with this format:
```
{
  "users": [
    // list of registered users 
  ]
}
```
This request does not require any parameters.

### commentList

Returns list of all comments with this format:
```
{
  "comments": [
    // list of comments 
  ]
}
```
This request does not require any parameters.

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

Returns stats about videos uploaded by user with format:
```
{
  "ok": *True or False depending on whether the user exists, type = bool*, 
  "viewCount": *total number of views in videos uploaded by user, type = int*,
  "videoCount": *count of videos uploaded by userm type = int*, 
  "likeCount": *total number of likes in videos uploaded by user, type = int*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### getFavourite

Returns list of videos that was liked by user with format:
```
{
  "ok": *True or False depending on whether the user exists, type = bool*, 
  "result": *list of liked videos, type = list*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### getUploadedVideos 

Returns list of videos that was uploaded by user with format:
```
{
  "ok": *True or False depending on whether the user exists, type = bool*, 
  "result": *list of uploaded videos, type = list*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### addComment

Adds comment to selected video, response format:. 
```
{
  "ok": *True or False, type = bool*, 
  "result": *list of all comments under this video, type = list*
}
```

Parameter | Description
----------|-------
```videoId``` | Id of selected video.
```commentText``` | Text of comment to add.

### getComments

Returns list of all comments depending to video, response format:
```
{
  "ok": *True or False, type = bool*, 
  "result": *list of all comments under this video, type = list*
}
```

Parameter | Description
----------|-------
```videoId``` | Id of selected video.

### getViewCount

Returns count of views under video, response format:
```
{
  "ok": *True or False, type = bool*, 
  "videoId": *list of all comments under this video, type = list*
}
```

Parameter | Description
----------|-------
```videoId``` | Id of selected video.


### exist

Returns true if user with passed login (phone or email) exist else false. 

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### likeVideo

Request that is used to like or dislike (in case video is already liked) video.
Response format:
```
{
  "ok": true,
  "likeCount": *number of likes for the video*,
  "isLiked": *true or false depending on whether the video is now liked* 
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.
```videoId``` | Id of video that should be liked.

### videoLikeCount

Request that returns number of likes of video and a flag indicating whether the video is liked .
Response format:
```
{
  "ok": true,
  "likeCount": *number of likes for the video*,
  "isLiked": *true or false depending on whether the video is now liked* 
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.
```videoId``` | Id of video.

### openVideo

Adds view to video, returns view and comment count with fromat:
```
{
  "ok": true,
  "viewCount": *number of views for the video*,
  "commentCount": *number of comments for the video*
}
```

Parameter | Description
----------|-------
```videoId``` | Id of video.

### getUser

Returns data of one used serialized to dictionary:
```
{
  "ok": true,
  "userData": *User object serialized to dictionary*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

## Admin requests

### blockUser

Moves user from userList to blockedUsers list, after this noone can login with this data.

Parameter | Description
----------|-------
```phone``` | Phone number of user to block.
```email``` | Email of user to block.

### blockedUserList

Returns list of all blocked users with this format:
```
{
  "users": [
    // list of blocked users data
  ]
}
```
This request does not require any parameters.

### resetPassword

Admin request that is used to reset password of user with selected login (phone or email).

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.

### deleteComment

Replaces comment's text with comething like "-This comment was deleted by administration-".

Parameter | Description
----------|-------
```id``` | Comment's identificator.

### getStats

Returns app statistic (loaded videos, created comments and registered users), format:
```
{
  "ok": true, 
  "videosUploadedCount": {
    "forLastDay": 0,
    "forLastWeek": 0,
    "forLastMonth": 0
  },
  "usersRegisteredCount": {
    "forLastDay": 0,
    "forLastWeek": 0,
    "forLastMonth": 0
  },
  "commentsLeftCount": {
    "forLastDay": 0,
    "forLastWeek": 0,
    "forLastMonth": 0
  }
}
```

This request does not require any parameters.

### addPromotionalVideo

Adds promotional video.

Parameter | Description
----------|-------
```title``` | Promotional video title.
```size``` | Size of promo video.
```length``` | Length of video.
```videoId``` | Id of video.
```maxShowCount``` | Max show count of video.
```displayOption``` | The way video will be shown: feed, openVideo, all, none (if none selected video will be hidden)

### updatePromotionalVideo

Updates promotional video (implementation of changing video title, maxShowCount and displayOption).

Parameter | Description
----------|-------
```videoId``` | Id of video we are going to update.
```title``` | Promotional video title.
```maxShowCount``` | Max show count of video.
```displayOption``` | The way video will be shown: feed, openVideo, all, none (if none selected video will be hidden)

### deletePromotionalVideo

Request for promotional video deleting.

Parameter | Description
----------|-------
```videoId``` | Id of video we are going to delete.

## User data editing

### editUserName

Request that is user to set new username to user with selected login (email/phone).
Response format:
```
{
  "ok": true,
  "userData": *User object serialized to dictionary*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.
```username``` | New username that will be set to user.

### editUserBirthDate

Request that is user to set new birth date to user with selected login (email/phone).
Response format:
```
{
  "ok": true,
  "userData": *User object serialized to dictionary*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.
```birthDate``` | New birth date that will be set to user.

### editUserCity

Request that is user to set new city to user with selected login (email/phone).
Response format:
```
{
  "ok": true,
  "userData": *User object serialized to dictionary*
}
```

Parameter | Description
----------|-------
```phone``` | Phone number of user.
```email``` | Email of user.
```city``` | New city that will be set to user.

## System parameters

### getParameters

Returns system configuration parameters, format:
```
{
  "ok": true, 
  "promotionalVideoFrequency": 0
}
```

This request does not require any parameters.

### setParameters

Sets system configuration parameters.

Parameter | Description
----------|-------
```promotionalVideoFrequency``` | A number equal to how many videos the ad will play.

## Link to the app repository
https://github.com/egor-baranov/Video-Sharing-App
