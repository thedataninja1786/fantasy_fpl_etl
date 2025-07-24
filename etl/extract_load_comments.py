from dataloader.load_data import DataLoader
from extractors.extract_posts_comments import CommentExtractor
from etl import (
    USER,
    PASSWORD,
    HOST,
    PORT,
    DBNAME,
    POST_LIMIT,
    SUBREDDIT_NAME,
    CLIENT_ID,
    SECRET,
    TIMEOUT,
    USER_AGENT,
    SchemaConfigs,
)


loader = DataLoader(user=USER, password=PASSWORD, host=HOST, port=PORT, dbname=DBNAME)


def etl_comments():
    print("Running comments etl...")
    try:
        CE = CommentExtractor(
            subreddit_name=SUBREDDIT_NAME,
            client_id=CLIENT_ID,
            secret=SECRET,
            timeout=TIMEOUT,
            user_agent=USER_AGENT,
            post_limit=POST_LIMIT,
        )

        print("Fetching comment data from posts...")
        comment_data = CE.fetch_comment_data(loader=loader)

        print("Writing comments to remote database...")

        loader.write_data(
            table_name="comments",
            data_rows=comment_data,
            column_names=SchemaConfigs.table_mapping["comments"],
            write_method="upsert",
            upsert_on=["id"],
        )

    except Exception as e:
        print(f"{etl_comments.__name__} - [ERROR] An error occurred {e}")


if __name__ == "__main__":
    etl_comments()
