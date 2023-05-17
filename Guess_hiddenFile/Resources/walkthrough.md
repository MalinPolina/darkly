# Guess(hidden file)

If we go to <http://192.168.31.133/robots.txt> we will find 2 folders disallowed - `/whatever` and `/.hidden`.
Let's check <http://192.168.31.133/.hidden/>

Here we have folders within folders with README files in them. Let's write a script to recursively traverse them, retrive README files and look in them for a flag.

DOESN'T WORK FOR ME

README with a flag: 
<http://192.168.31.133/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README>

> Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

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