from tweepy import API, OAuthHandler
from tweepy.models import Status
from typing import Dict

def init_twitter_api(consumer_key        : str, 
                     consumer_secret     : str, 
                     access_token        : str, 
                     access_token_secret : str) -> API:
    r"""Initialize client of Twitter API.
    
    Args:
        consumer_key (str): Consumer key of Twitter API.
        consumer_secret (str): Consumer secret of Twitter API.
        access_token (str): Access token of Twitter API.
        access_token_secret (str): Access token secret of Twitter API.
    
    Returns:
        API: Client of twitter API.
    """
    # Initialize OAuthHandler of Twitter API
    auth = OAuthHandler(consumer_key, consumer_secret)

    # Set access token to OAuthHandler
    auth.set_access_token(access_token, access_token_secret)

    # Initialize API client with OAuthHandler
    auth_api = API(auth)
    return auth_api

def status_parser(status: Status) -> Dict[str, str]:
    r"""parse tweepy.models.Status to Dictionary
    
    Args:
        status (Status): Object responsed from twitter API.
    
    Returns:
        Dict[str, str]: Parsed dictionary.
    """
    # Get json body from status object
    json_body = status._json

    # Create a json body to be returned
    return_body = dict()

    # Get information from json_body
    return_body["username"] = json_body.get("user", {}).get("name")
    return_body["message"] = json_body.get("text")
    return_body["url"] = json_body.get("entities", {}).get("urls", [{}])[0].get("url")
    return_body["retweet_count"] = json_body.get("retweet_count")
    return_body["favorite_count"] = json_body.get("favorite_count")
    
    return return_body
