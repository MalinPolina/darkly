# Redirect

At the bottom of the main page we find links to social networks.
As you can see from the markup code, the redirect page is used with the site parameter.
```
<ul class="icons">
	<li>
        <a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a>
    </li>
	<li>
        <a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a>
    </li>
    <li>
        <a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a>
    </li>
</ul>
```
![redirect](./img/redirect.png)
By changing the site parameter to your own, we get a flag.

## Explanation
Attack type: [Unvalidated Redirects](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
> Unvalidated redirects and forwards are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input.
> By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials.

## How to fix it
> Avoid using redirects and forwards.
