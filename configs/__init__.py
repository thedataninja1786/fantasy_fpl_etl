class PostAPIConfigs:
    subreddit_name = "FantasyPL"
    timeout = 10
    ratelimit_seconds = 60
    post_limit = 250 # most recent posts

class SchemaConfigs:
    table_mapping = {
        "posts":[
            "id",
            "title",
            "author",
            "flair",
            "selftext",
            "subreddit",
            "score",
            "num_comments",
            "created_utc",
        ],
        "comments":[
            "id",
            "post_id",
            "parent_id",
            "body",
            "author",
            "score",
            "created_utc"
        ],
        "posts_embeddings":[
            "id",
            "title",
            "author",
            "flair",
            "selftext",
            "created_utc",
            "embeddings"
        ]
    }   