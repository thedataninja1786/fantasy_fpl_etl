import json
from openai import OpenAI
from typing import Optional, Dict
import re
import html

class TextEmbedder:
    def __init__(self, client: OpenAI):
        self.client = client
    
    def clean_comment(self,text: str) -> str:
        if not text:
            return ""
        
        text = text.replace("\n", " ")

        # Unescape HTML entities (e.g. &amp; -> &)
        text = html.unescape(text)

        # Remove URLs
        text = re.sub(r'https?://\S+|www\.\S+', '', text)

        # Remove emails (optional, in case you have them)
        text = re.sub(r'\S+@\S+', '', text)

        # Remove HTML tags (in case you have scraped content)
        text = re.sub(r'<.*?>', '', text)

        # Remove emojis and non-ASCII symbols (optional — depends on your needs)
        text = re.sub(r'[^\x00-\x7F]+', '', text)

        # Remove control characters (non-printable ASCII)
        text = re.sub(r'[\x00-\x1F\x7F]', '', text)

        # Normalize multiple spaces and line breaks into single space
        text = re.sub(r'\s+', ' ', text)

        # Strip leading/trailing spaces
        text = text.strip()

        return text

    def generate_embeddings(self, text: str):
        """ Creates embeddings for 'selftext' of a post for performing similarity search 
            based on user queries.
        """
        try:
            text = self.clean_comment(text)
            return (
                self.client.embeddings.create(
                    input=[text], model="text-embedding-3-small"
                )
                .data[0]
                .embedding
            )
        except Exception as e:
            print(text)
            print(
                f"{self.generate_embeddings.__name__} [ERROR] - generating embedding failed: {e}"
            )
            return None