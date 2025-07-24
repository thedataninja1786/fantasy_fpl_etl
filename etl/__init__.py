from utils.utilities import get_env_variable
from configs import PostAPIConfigs, SchemaConfigs
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# DB CONFIGS
USER = get_env_variable("DB_USER")
PASSWORD = get_env_variable("DB_PASSWORD")
HOST = get_env_variable("DB_HOST")
PORT = get_env_variable("DB_PORT")
DBNAME = get_env_variable("DB_NAME")
API_KEY = get_env_variable("API_KEY")

# Subreddit Configs
REDDIT_USERNAME = get_env_variable("REDDIT_USERNAME")
SUBREDDIT_NAME = PostAPIConfigs.subreddit_name
CLIENT_ID = get_env_variable("CLIENT_ID")
SECRET = get_env_variable("CLIENT_SECRET")
TIMEOUT = PostAPIConfigs.timeout
USER_AGENT = f"script:{SUBREDDIT_NAME}:1.0 (by u/{REDDIT_USERNAME})"
POST_LIMIT = PostAPIConfigs.post_limit

# Clients
client = OpenAI(api_key=API_KEY)
