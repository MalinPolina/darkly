## Description

Little project to familiarize ourselves with basics of cyber security in the field of WWW. By looking for flags on the provided website we explored general vulnerabilities, dicovered OWASP and found out inner workings of websites in general.

## Solutions

| **Name**              | **Contibutor** |
|-----------------------|----------------|
| SQL injection basic   |     rvinnie    |
| SQL injection advanced|     rvinnie    |
| Include               |     daniseed   |
| XSS basic             |     rvinnie    |
| XSS advanced          |     rvinnie    |
| Cookies               |     rvinnie    |
| Spoof(curl)           |     daniseed   |
| Admin(htpasswd)       |     daniseed   |
| Bruteforce(member)    |     daniseed   |
| File upload           |     rvinnie    |
| Redirect              |     rvinnie    |
| Guess(hidden file)    |     daniseed   |
| Survey                |     daniseed   |
| Recover               |     daniseed   |

## Where to start

First few vulnerabilities were discovered simply by running `nikto`:

```
darkly$  nikto -p 80 -host [VM_IP]
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          [VM_IP]
+ Target Hostname:    [VM_IP]
+ Target Port:        80
+ Start Time:         2023-05-09 17:21:27 (GMT3)
---------------------------------------------------------------------------
+ Server: nginx/1.4.6 (Ubuntu)
+ Cookie I_am_admin created without the httponly flag
+ Retrieved x-powered-by header: PHP/5.5.9-1ubuntu4.29
+ The anti-clickjacking X-Frame-Options header is not present.
+ Server leaks inodes via ETags, header found with file /lTjbVLX8.types, fields: 0x60db63b9 0x3cf
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-3268: /whatever/: Directory indexing found.
+ File/dir '/whatever/' in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ File/dir '/.hidden' in robots.txt returned a non-forbidden or redirect HTTP code (301)
+ "robots.txt" contains 2 entries which should be manually viewed.
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /includes/: This might be interesting...
+ OSVDB-3093: /admin/index.php: This might be interesting... has been seen in web logs from an unknown scanner.
+ 6544 items checked: 9 error(s) and 11 item(s) reported on remote host
+ End Time:           2023-05-09 17:21:40 (GMT3) (13 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
