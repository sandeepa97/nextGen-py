# Explore Variables and Data Types in Java , C# and PHP
=======================================================

=======================================================
## Java
=======

Java variable naming conventions
--------------------------------

> case sensitive
> a variable name can be any legal identifier (unicodes, $ , _)
> can begin with a digit, $ or _ but start variable name with a letter is the best practice
> can not use keywords or reserved words
> cammel notation and _ for seperating words is the best practice

Java data types
---------------

> Integer (whole number)    >>  int myNum = 5 ; 
> Floating point number     >>  float myFloatNum = 5.99f ;
> Character                 >>  char myLetter = 'D' ;
> Boolean                   >>  boolean myBool = true ; 
> String                    >>  String myText = "Hello" ; 

--Primitive Data Types--

> byte    //integer type
> short   //integer type
> int     //integer type
> long    //integer type

> float   //floating point type
> double  //floating point type

> boolean
> char

--Non-Primitive Data Types--

> Strings
> Arrays
> Classes
> Interface

Declaring variables
-------------------

type variable = value;

eg: 
String name = "Sandeepa";
System.out.println(name);


==========================
## C#
======

C# variable naming concentions
------------------------------

> case sensitive
> do not use single character variables such as i, n, s | but use index, temp etc
> Pascal casing for Class names eg : HelloWorld
> Pascal casing for Method names  eg : SayHello
> Camel casing for variables and method parameters eg : totalCount , fullMessage
> use I with camel casing for interfaces eg : IEntity

C# data types
-------------

> Integer (whole number)    >>  int myNum = 5 ; // long
> Floating point number     >>  double myDoubleNum = 5.99f ; // float
> Character                 >>  char myLetter = 'D' ;
> Boolean                   >>  bool myBool = true ; 
> String                    >>  string myText = "Hello" ; 

--Numbers--

> int // Integer type
> long // Integer type
> float // Floating point type
> double // Floating point type

Declaring variables
-------------------

string greeting = "Hello World";
Console.WriteLine(greeting);


============================
## PHP
======

PHP variable naming conventions
-------------------------------

> A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume)
> A variable starts with the $ sign, followed by the name of the variable
> A variable name must start with a letter or the underscore character
> A variable name cannot start with a number
> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
> Variable names are case-sensitive ($age and $AGE are two different variables)

PHP data types
--------------

> String    >>> $x = "Hello world!";
> Integer   >>> $x = 5985;
> Float     >>> $x = 10.365;
> Boolean   >>> $x = true;
> Array     >>> $cars = array("Volvo","BMW","Toyota");
> Object    >>> $myCar = new Car("black", "Volvo");
> NULL      >>> $x = null;
> Resource  >>> a database call...

Declaring variables
-------------------

<?php

$name = "Sandeepa";
echo $name;

?>


