#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import time
import glob
import argparse
import requests
import logging
from tqdm import tqdm

THREADS = 15
TIMEOUT = 60

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.WARNING,  # Debug logging change to logging.INFO
    datefmt="%Y-%m-%d %H:%M:%S",
)


class StorageUploader:
    FILES = []
    FILECOUNT = 0
    DELETE_LOCAL = False

    def delete_local_file(self, path):
        logging.info(f"Deleting {path}")
        os.unlink(path)

    def auth_header(self):
        return {"AccessKey": self.ACCESS_KEY}

    def upload(self, path):
        url = f"{self.BASE_URL}/{self.STORAGE_ZONE}/{path[1]}"

        with open(path[0], "rb") as fin:
            for retry in range(0, 3):
                req = requests.put(
                    url=url, headers=self.auth_header(), data=fin, timeout=TIMEOUT
                )

                try:
                    req.raise_for_status()
                except Exception:
                    logging.exception(
                        f"Uploading {path[0]} into {path[1]} failed, try {retry + 1}/3",
                        exc_info=True,
                    )

                if req.status_code == 201:
                    logging.info(
                        f"Uploading {path[0]} into {path[1]} succeeded in {req.elapsed.total_seconds()}, try {retry + 1}/3"
                    )
                    if self.DELETE_LOCAL:
                        self.delete_local_file(path[0])
                    break
                else:
                    logging.warning(
                        f"Uploading {path[0]} into {path[1]} failed, status code {req.status_code}, try {retry + 1}/3"
                    )

                time.sleep(5 ** (retry + 1))

    def test_connectivity(self):
        req = requests.get(
            f"{self.BASE_URL}/{self.STORAGE_ZONE}/",
            headers=self.auth_header(),
            timeout=TIMEOUT,
        )

        req.raise_for_status()

        if req.status_code == 200:
            logging.info("Connectivity test successful")
        else:
            logging.error(
                f"Error while connecting to storage, status code {req.status_code}"
            )

    def uploader(self):
        with tqdm(total=self.FILECOUNT) as pbar:
            with ThreadPoolExecutor(max_workers=THREADS) as ex:
                logging.warning("Submitting tasks, please wait...")
                futures = [ex.submit(self.upload, url) for url in self.FILES]
                logging.warning("Tasks submitted, starting upload")
                for future in as_completed(futures):
                    result = future.result()
                    pbar.update(1)

    def parse_path(self, paths):
        for path in paths:
            for filename in [
                x for x in glob.iglob(path + "**", recursive=True) if os.path.isfile(x)
            ]:
                target_path = f"{filename[len(path):]}"
                self.FILES.append((filename, target_path))
                self.FILECOUNT += 1

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="CLI uploader for Bunny Storage", allow_abbrev=True
        )

        parser.add_argument(
            "--storagezone", type=str, help="Storage zone name", required=True
        )
        parser.add_argument(
            "--accesskey", type=str, help="Storage access key / password", required=True
        )
        parser.add_argument(
            "--deletelocal",
            help="Deletes local files once successfully uploaded",
            action="store_true",
        )
        parser.add_argument("--region", help="storage region", default="storage")
        parser.add_argument("PATH", type=str, help="File path to upload", nargs="+")
        parser.set_defaults(deletelocal=False)

        args = parser.parse_args()

        if len(vars(args)) < 1:
            parser.print_help()
            return

        self.ACCESS_KEY = args.accesskey
        self.STORAGE_ZONE = args.storagezone
        self.DELETE_LOCAL = args.deletelocal
        if args.region == "storage":
            self.BASE_URL = "http://storage.bunnycdn.com"
        else:
            self.BASE_URL = f"http://{args.region}.storage.bunnycdn.com"
        logging.warning("Testing connectivity to storage")
        self.test_connectivity()

        logging.warning("Gathering a list of files to upload")
        self.parse_path(args.PATH)

        logging.warning(f"Uploading {self.FILECOUNT} files")

        self.uploader()


if __name__ == "__main__":
    StorageUploader()
