import sys
import time

import requests

COUNT_REQUEST = 10
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]
    speed_measure(url)

def speed_measure(url: str) -> bool:
    total_time: float = 0.0
    total_bytes: int = 0

    for i in range(1, COUNT_REQUEST + 1):
        try:
            start = time.perf_counter()
            r = requests.get(url, headers=HEADERS)
            r.raise_for_status()
            elapsed = time.perf_counter() - start
        except requests.RequestException as e:
            print(f"{i=} ошибка ({e})")
            continue

        size = len(r.content)
        total_time += elapsed
        total_bytes += size

    avg_time = total_time / COUNT_REQUEST
    speed_mbs = (total_bytes / total_time) / (1024 * 1024)
    print(f"Среднее время запроса: {avg_time:.3f} сек")
    print(f"Скорость: {speed_mbs:.2f} МБ/с")


if __name__ == "__main__":
    main()
