# Task:

Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

## Expected output
```bash
kevinkoech357@kevinkoech357:~/ALX/alx-interview/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5127
301: 2
401: 4
403: 1
405: 1
500: 2
File size: 9680
200: 1
301: 4
401: 6
403: 2
404: 2
405: 2
500: 3
File size: 13416
200: 2
301: 5
400: 1
401: 7
403: 3
404: 4
405: 5
500: 3
File size: 18525
200: 2
301: 7
400: 3
401: 7
403: 5
404: 6
405: 5
500: 5
^CTraceback (most recent call last):
  File "/home/kevinkoech357/ALX/alx-interview/0x03-log_parsing/./0-generator.py", line 8, in <module>
File size: 19089
200: 2
301: 7
400: 3
401: 8
403: 5
404: 6
405: 5
500: 5
Traceback (most recent call last):
  File "/home/kevinkoech357/ALX/alx-interview/0x03-log_parsing/./0-stats.py", line 30, in <module>
    sleep(random.random())
KeyboardInterrupt
    for line in sys.stdin:
KeyboardInterrupt
```
