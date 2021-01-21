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
    codes = dict()
    missed = 0

    def send_request():
        while not start: continue
        if method == 'get':
            response = requests.get(url, headers=headers, timeout=timeout)
        else:
            response = requests.request(method, url, headers=headers, body=body, timeout=timeout)
        if response.status_code in codes.keys():
            codes[response.status_code] += 1
        else:
            codes[response.status_code] = 1

    for i in range(count):
        try:
            threading.Thread(target=send_request).start()
        except TimeoutError:
            missed += 1

    start = True
    while threading.active_count() > 1:
        continue
    click.echo(str(count) + " Requests sent.\nNumber of timeouts: " + str(missed) + "\nStatus codes:")
    print(codes)


if __name__ == "__main__":
    main()
