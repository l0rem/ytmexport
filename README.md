# YouTube Music Export
This tool allows to convert your YT Music "Liked Songs"-playlist into a user-created playlist,
which helps sharing songs that You like with your friends.

## Usage
In order to access your YT Music library you are going to need auth headers from your browser session.
Follow [THIS](https://ytmusicapi.readthedocs.io/en/latest/setup.html) guide and store your headers 
locally as a JSON file.
```python
from core import YtEngine

ytm = YtEngine()
ytm.export_likes()
```

## TODOs:
 - Allow exporting playlists to Apple Music.
 - User interface with Django.