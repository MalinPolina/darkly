# Recover

Go to `Sign In` page <http://192.168.31.133/?page=signin> and then to <http://192.168.31.133/?page=recover#> by clicking `I forgot my password`. If we click `Submit` nothing happens.

Let's look at the source code on recover page. We have a hidden input for submit:

`
[...]
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value= "Submit">
</form>
[...]
`

So the recovery password is sent to *webmaster@borntosec.com*.
We can remove this hidden input with developer tools in Source and then click on `Submit`.

We have our flag

------------ToDo------------

## Explanation

robots.txt is accessible

## How to fix it

