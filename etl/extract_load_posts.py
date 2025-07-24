from extractors.extract_posts import PostExtractor
from dataloader.load_data import DataLoader
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


def etl_posts():
    print("Running posts etl...")
    try:
        PE = PostExtractor(
            subreddit_name=SUBREDDIT_NAME,
            client_id=CLIENT_ID,
            secret=SECRET,
            timeout=TIMEOUT,
            user_agent=USER_AGENT,
            post_limit=POST_LIMIT,
        )

        print("Fetching posts...")
        posts_data = PE.fetch_post_data()

        loader = DataLoader(
            user=USER, password=PASSWORD, host=HOST, port=PORT, dbname=DBNAME
        )
        print("Writing posts to remote database...")

        loader.write_data(
            table_name="posts",
            data_rows=posts_data,
            column_names=SchemaConfigs.table_mapping["posts"],
            write_method="upsert",
            upsert_on=["id"],
        )
    except Exception as e:
        print(f"{etl_posts.__name__} - [ERROR] An error occurred {e}")


if __name__ == "__main__":
    etl_posts()
