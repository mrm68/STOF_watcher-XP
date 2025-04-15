# main.py

from pathlib import Path
from typing import List, Optional
from abc import ABC
from .crawlers import Crawler
from config_handler import config_handler


class i_watcher(ABC):
    def start_watch(self):
        pass

    def watch(self):
        pass


class watcher(i_watcher):
    def __init__(self, crawler: Optional[Crawler] = Crawler,
                 header=None, crawl_detail=None):
        self.crawler = crawler()
        self.header = header
        self.crawl_detail = crawl_detail
        self.url = self._build_url(header)
        self.storage_path = Path("last_seen_id.txt")

    def _build_url(self, header=None):
        if hasattr(header, "base_url") and hasattr(header, "tag"):
            return (f"{header.base_url}/questions/tagged/{header.tag}?page=1")

    def _load_last_id(self):
        if self.storage_path.exists():
            return int(self.storage_path.read_text())
        return 0

    def _save_last_id(self, q_id: int):
        self.storage_path.write_text(str(q_id))

    def _filter_new_questions(self, question: List[Question]):
        pass

    def start_watch(self):
        print("crawl_detail")
        print(vars(self.crawl_detail))
        print("header")
        print(vars(self.header))
        self.watch()

    def watch(self):
        print("I'm watching")
        print(self.url)
        while True:
            pass


def main():
    c_handler = config_handler()

    watcher1 = watcher(header=c_handler.get_crawl_config(),
                       crawl_detail=c_handler.get_parse_config())
    watcher1.start_watch()


if __name__ == "__main__":
    main()
