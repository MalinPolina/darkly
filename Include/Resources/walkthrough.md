# Include

All websites running on UNIX contain a folder `/etc/passwd` which contains the attributes of each user/account on a Linux or another Unix-like operating system.

By adding `/?page=../` to our url and using the displayed indices we can go back to the `/etc/passwd`.

Path: <http://192.168.31.135/?page=../../../../../../../etc/passwd>

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```

## Explanation

Attack type: [Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

> A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files. 

## How to fix it

1) Do not use user input when using file system calls
2) Use indexes rather than actual portions of file names when templating or using language files
3) Ensure the user cannot supply all parts of the path – surround it with your path code
4) Validate the user’s input by only accepting known good – do not sanitize the data
5) Use chrooted jails and code access policies to restrict where the files can be obtained or saved to
6) If forced to use user input for file operations, normalize the input before using in file io API’s, such as normalize().