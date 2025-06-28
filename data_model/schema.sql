-- Fact: post-level metrics table
CREATE TABLE IF NOT EXISTS POSTS(
    ID TEXT PRIMARY KEY,
    TITLE TEXT,
    AUTHOR TEXT,
    FLAIR TEXT,
    SELFTEXT TEXT,
    SUBREDDIT TEXT,
    SCORE BIGINT, 
    NUM_COMMENTS BIGINT,
    CREATED_UTC TIMESTAMPTZ,
    EMBEDDINGS vector(1536),
    PROCESSING_TIMESTAMP TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Fact: comments-level data
CREATE TABLE IF NOT EXISTS COMMENTS(
    ID TEXT PRIMARY KEY,
    POST_ID TEXT NOT NULL 
            REFERENCES POSTS(ID)
            ON DELETE CASCADE,
    PARENT_ID TEXT,
    BODY TEXT,
    AUTHOR TEXT,
    SCORE BIGINT,
    CREATED_UTC TIMESTAMPTZ,
    PROCESSING_TIMESTAMP TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Create index on posts for fast search
-- if you don't specify WITH (lists = ...), PostgreSQL uses a very small default
-- (maybe just 1), which hurts performance and accuracy.
CREATE INDEX posts_embedding_idx
ON posts
USING ivfflat (embeddings vector_cosine_ops)
WITH (lists = 100);  -- Tune this depending on dataset size

-- controls the accuracy vs. speed tradeoff. More probes = better results, slower search
SET ivfflat.probes = 10;
