from typing import Final

users_path = "components/database/data/users.json"
blocked_users_path = "components/database/data/blocked_users.json"

videos_path = "components/database/data/videos.json"

comments_path = "components/database/data/comments.json"

notifications_path = "components/database/data/notifications.json"

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Content-Type": "application/json; charset=utf-8",
}

SECONDS_IN_DAY: Final = 3600 * 24
SECONDS_IN_WEEK: Final = SECONDS_IN_DAY * 7
SECONDS_IN_MONTH: Final = SECONDS_IN_DAY * 30
