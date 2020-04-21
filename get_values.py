import urllib.request
import json
import os

from pathlib import Path

if __name__ == "__main__":
    # create env_files directory
    dir_path = Path("../env_files")
    os.makedirs(dir_path, exist_ok=True)

    url = "http://localhost:8200/v1/app/data/postgres"
    token = "s.sfcBKH3eFF4S6D3ApW8mBhSa"
    headers = {"X-Vault-Token": token}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))

        postgres_secret = data['data']['data']
        postgres_env_path = dir_path / "postgres.env"
        with open(postgres_env_path, 'w') as f:
            for k, v in postgres_secret.items():
                f.write(f"{k}={v}\n")
