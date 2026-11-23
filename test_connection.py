#import os

#from dotenv import load_dotenv
# read the .env file
#from openai import OpenAI
#Import OpenAI SDK.

#load_dotenv()

#client = OpenAI(
    #api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    #base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
#)

#response = client.responses.create(
    #model=os.getenv("MODEL_DEPLOYMENT"),
    #input="Say Hello"
#)

#print(response.output_text)#

import os

from dotenv import load_dotenv

from openai import OpenAI

from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider
)

load_dotenv()

endpoint = os.getenv(
    "AZURE_OPENAI_ENDPOINT"
)

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)