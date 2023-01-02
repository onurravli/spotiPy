import json
import requests


class person():
    def __init__(self, timestamp, user, track) -> None:
        self.timestamp = timestamp
        self.user = user
        self.track = track
        pass

    def getUser(self):
        userName = self.user["name"]
        return f"{userName}"

    def getTrack(self):
        trackName = self.track["name"]
        artist = self.track["artist"]["name"]
        album = self.track["album"]["name"]
        context = self.track["context"]["name"]
        return f"{trackName} by {artist} from {album} in {context}"


def getWebAccessToken(spdc) -> str:
    req = requests.get(url="https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                       headers={"Cookie": f"sp_dc={spdc}"})
    return json.loads(req.text)['accessToken']


def getFriendActivity(getWebAccessToken) -> str:
    res: str = ""
    req = requests.get(url="https://guc-spclient.spotify.com/presence-view/v1/buddylist",
                       headers={"Authorization": f"Bearer {getWebAccessToken}"})
    return json.loads(req.text)


spcd = ""
webAccessToken = getWebAccessToken(spcd)
friendActivity = getFriendActivity(webAccessToken)

friends = friendActivity['friends'].__reversed__()  # type: ignore

for friend in friends:
    timestamp = friend['timestamp']  # type: ignore
    user = friend['user']  # type: ignore
    userName = user['name']  # type: ignore
    userImage = user['imageUrl']  # type: ignore
    track = friend['track']  # type: ignore
    trackName = track['name']  # type: ignore
    trackAlbum = track['album']['name']  # type: ignore
    artistName = track['artist']['name']  # type: ignore
    contextName = track['context']['name']  # type: ignore

    user = person(timestamp, user, track)
    print(f"{user.getUser()} is listening to {user.getTrack()}")
