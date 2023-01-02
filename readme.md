## spotiPy

spotiPy is a Python wrapper for the Spotify Web API. It is a work in progress and is not yet complete. It is currently in the alpha stage of development.


### Installation

To install spotiPy, simply run the following command:

    pip install spotiPy


### Usage

To use spotiPy, you must first get your Spotify SP_DC cookie. You can do this by logging into Spotify and then going to [https://open.spotify.com/get_access_token?reason=transport&productType=web_player](https://open.spotify.com/get_access_token?reason=transport&productType=web_player). Copy the value of the cookie named "sp_dc" and paste it into the following code:

```python
spcd = "" # Paste your SP_DC cookie here
webAccessToken = getWebAccessToken(spcd)
friendActivity = getFriendActivity(webAccessToken)
```