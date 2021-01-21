# Send HTTP Requests at same time.

## How to send same request for n times at same time:
    python main.py [url] [options]
| Option    | shortCMD | type   | default | help              |
|-----------|----------|--------|---------|-------------------|
| --method  | -m       | string | get     | request's method. |
| --body    | -b       | string |         | request's body    |
| --headers | -h       | string |         | request's headers |
| --count   | -c       | int    | 10      | number of threads |
| --timeout | -t       | float  | 2.5     | request's timeout |
## Send postman collection requests at the same time:
///TODO