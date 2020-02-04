from shank.config  import Settings
from shank         import __version__

def test_settings():
    settings = Settings()
    settings.get("version") == __version__