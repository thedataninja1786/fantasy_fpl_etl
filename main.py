from etl.extract_load_posts import etl_posts
from etl.extract_load_comments import etl_comments
from etl.create_load_posts_embeddings import posts_embeddings

def main():
    etl_posts()
    posts_embeddings()
    etl_comments()

if __name__ == "__main__":
    main()
