import threading
import requests
import click


@click.command()
@click.argument('url')
@click.option('--method', '-m', default='get', help='Request method')
@click.option('--body', '-b', default='', help='Request body')
@click.option('--headers', '-h', default='', help='Request headers')
@click.option('--count', '-c', default=10, help='Number of threads')
@click.option('--timeout', '-t', default=2.50, help='Request timeout time')
def main(url, method, body, headers, count, timeout):
    start = False

    def send_request():
        while not start: continue
        if method == 'get':
            requests.get(url, headers=headers, timeout=timeout)
        else:
            requests.request(method, url, headers=headers, body=body, timeout=timeout)
    for i in range(count):
        threading.Thread(target=send_request).start()

    start = True


if __name__ == "__main__":
    main()
