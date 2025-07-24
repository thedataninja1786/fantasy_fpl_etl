from openai_embeddings.embedder import TextEmbedder
from openai_embeddings.create_embeddings import PostAnalyzer
from dataloader.load_data import DataLoader
from etl import client, USER, PASSWORD, HOST, PORT, DBNAME, POST_LIMIT, SchemaConfigs


embedder = TextEmbedder(client=client)

# Instances
loader = DataLoader(user=USER, password=PASSWORD, host=HOST, port=PORT, dbname=DBNAME)
analyzer = PostAnalyzer()


def posts_embeddings():
    print("Running creating embeddings for posts...")
    try:

        new_posts = analyzer.find_new_posts(loader=loader, post_limit=POST_LIMIT)

        print(f"Found {len(new_posts)} posts to embedd.")

        results = analyzer.process_posts(embedder=embedder, posts=new_posts)
        if results:

            print(f"{len(results)} have been processed.")
            print("Writing data to remote database...")

            loader.write_data(
                table_name="posts_embeddings",
                data_rows=results,
                column_names=SchemaConfigs.table_mapping["posts_embeddings"],
                write_method="upsert",
                upsert_on=["id"],
            )
        else:
            print("No results to write; exiting...")

    except Exception as e:
        print(f"{posts_embeddings.__name__} - [ERROR] An error occurred {e}")


if __name__ == "__main__":
    posts_embeddings()
