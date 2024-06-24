from pathlib import Path

basedir = Path(__file__).parent.parent


# BaseConfigクラスを作成する
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2BsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))


# BaseConfigコンフィグクラスを継承してLocalConfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# BaseConfigクラスを継承しTestConfigクラスを作成する
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


# config辞書にマッピングする
config = {
    "testing": TestConfig,
    "local": LocalConfig,
}
