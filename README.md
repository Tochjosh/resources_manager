# ASSESSMENTS

Below are exercises that you are expected to complete and provide solutions to.
Happy hacking, cheers

## Secure a Resource

You just resumed after a 3 weeks leave, you met most of the company's employees from different departments talking about the company’s data that was breached. You quickly ran into the directors office to get the detailed context of what happened. The director affirmed the incident that the company's most valuable resource and business logic has been sold out to our competitor.

As the most senior engineer the company has, the director wants you to secure the resources and only allow admin and super admin to view and access it.

Luckily for us the company already has a database where all the employee records are stored, an authentication function that authenticates users and a function that returns the company's most valuable resource.

Since the company software has already been built, tested and deployed. It is not advisable to manually change or alter all these implementations and modules that can lead to re-writing the whole codebase which we would not want to do and also to follow Open/Close principles that says software should Open for Extension but Close for modification.

In this task you are to write a decorator function that will secure the company’s most valuable resources and also logs all employee information that access or tried to access the resource
These are the detailed specifications of what the company wants

- Only user with admin and super admin role should be able to to view the resource
- Logs admin and super admin information to a file named `access_granted.txt`. The information to be logged are full name, role, date, time e.g `Admin Oluwatosin Ayodele viewed company resources on 1/4/2021 at 10:30`
- All other employee should not have access to the resource
- Return a warning message to all other employees who attempt to access the resource `You are not allowed to view this resource`
- Logs other employees details to a file named `access_denied.txt` with the following information full name, role, date, time e.g `Marketer Favour Nnabue tried to view company most valuable resources on 10/4/2021 at 10:30`
- If the resource was tried to be accessed by an anonymous user return a message that reads `Only staff can access this resource`

Note: The time and date should be current time the user access or tried to access the resource.

## Working With Regular Expression

### Overview

This task deals with implementing functionalities for parsing email addresses. Parsing in this context simply means looking through email address strings to pick out important and useful information.

### Parsing Email Addresses

Email addresses are usually in the format: `username@domain`. Ex. `johndoe@gmail.com`, `jane+doe@yahoo.com`, etc. This means that there are two(2) useful information we will need out of email addresses, namely `username` and `domain`

Given the email address (`johndoe@gmail.com`), we will have the dictionary below as the output of the parsing

```python

{
  'username': 'johndoe',
  'domain': 'gmail.com'
}

```

Also, given the email address (`jane+doe@yahoo.com`), we will have the dictionary below as the output of the parsing

```python

{
  'username': 'jane+doe',
  'domain': 'yahoo.com'
}

```

When writing the logic for parsing email addresses, below are CONSTRAINTS you need to put into consideration

- Usernames will be made up of alphabets or alphanumerics. Ex. `john`, `johndoe`, `john123`. Note that usernames cannot start with a number
- Usernames should also support only the `+` character in between as in example 2 above
- Domains will always end in `.com`, Ex. `gmail.com`, `yahoo.com`, `bz2.com`, etc.
- The part before `.com` in domains will be made up of alphabets or alphanumerics, Ex. `gmail`, `bz2`, `dom555`, etc. Note that domains cannot start with a number

To complete the implementation of the `email_parser` function defined in the `email_parser.py` module, you will need to

1. Provide a regex pattern 
2. Complete the implementation to do the expected parsing
3. Return `None` for emails that do not match the regex pattern
