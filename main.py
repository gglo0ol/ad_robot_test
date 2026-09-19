import requests
import sys
import time

COUNT_REQUEST = 2
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

def main():
    url = sys.argv[1]
    speed_measure(url)


def speed_measure(url: str):
    total_time :float = 0.0
    total_bytes :int = 0

    for i in range(1, COUNT_REQUEST + 1):
        start = time.time()
        r = requests.get(url,   headers=HEADERS)
        r.raise_for_status()
        end = time.time()
        elapsed = end - start
        size = len(r.content)

        total_time += elapsed
        total_bytes += size
        print(f"Запрос {i + 1}: {elapsed:.3f} сек, {size / 1024:.1f} КБ")

        time.sleep(0.5)

    avg_time = total_time / COUNT_REQUEST
    speed_mbs = (total_bytes / total_time) / (1024 * 1024)

    print(f"Среднее время запроса: {avg_time:.3f} сек")
    print(f"Всего скачано: {total_bytes / (1024 * 1024):.2f} МБ")
    print(f"Скорость: {speed_mbs:.2f} МБ/с")


if __name__ == "__main__":
    main()
