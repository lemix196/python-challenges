## My solutions of most popular coding problems

This is repository of all "smaller" scripts (so called __*challenges*__) provided by me. That repository convention is to place every solution in other branch.

### Current challenge list

1. __balanced_string__

Set of functions with the core __solution__ function that allows to check whether given string has *__balanced string__* slice in it. Any string slice is *__balanced__* if every character in that set of characters occurs at least once in upper and lowercase. 

Examples of *__balanced strings__*:
* "aBbA" 
* "ZdRXXDxzr" (at least one __z__ and __Z__, __d__ and __D__, __r__ and __R__, __x__ and __X__)
* "AcZCbaBz" (at least one __a__ and __A__, __b__ and __B__, __c__ and __C__, __z__ and __Z__)

The __solution__ function not only checks if given string is balanced, but mainly checks every possible consecutive slice of given string (from the shortest possible of length of 2 to the full string length) and returns length of the shortest slice of characters that fulfills the rule of balanced string. If there are not any balanced strings, function returns -1.