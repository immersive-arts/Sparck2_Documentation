# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &#123;expressions}
{expressions} can be used inisde quescript. {expressions} are in realtime evaluated operations and functions that can use variables.

{expressions} always need to be inside a {} bracket. They can use variables, strings, operands and functions. Strings can be added to each other like numbers, and if the result is a string, a string is returned.

TIP: If {expressions} dont behave as you would expect, send a `reset` message. This clears all the variables.

### [Usage](QS1-Expr-Usage.md)  
### [Variables](QS1-Expr-Variables.md)
### [Arrays](QS1-Expr-Arrays.md)
### SystemVariables

static Variables

    PI
    TRUE
    FALSE

frame dependent variables (script-node memory)

    $HOUR   current hours
    $MIN    current minutes
    $SEC    current seconds
    $MILLI  current millis

timer Variable - requires the use of &lt;[timer](QS1-timer-cmd.md)&gt; (que-node memory)

    $TIMER  milliseconds since the timer was started


### Operators

    *   multiply               \
    /   division                \  also works with arrays and combinations of single values and arrays
    +   addition                /
    -   substraction           /

    ^   power of
    %   modulo

    ==  equal
    !=  not equal
    gt  (>) greater than        \  Carefull: using < or > inside an {expr} will cause
    st  (<) smaller than         \     a parsing error of Quescript. This is due to
    ge  (>=) greater equal than  /     the fact that those characters are reserved
    se  (<=) smaller equal than /      for xml-tags.
    &&  logical AND
    ||  logical OR

    =   assign value to a variable: var = value
    ->  assign a reference to a variable: var -> function()

### Functions

    RANDOM()                returns 0..1
    SIN(rad)                sine of angle
    COS(rad)                cosine of angle
    TAN(rad)                tangens of angle
    ASIN(val)               ArcSine of value
    ACOS(val)               ArcCosin of value
    ATAN(val)               ArcTangens of value
    SINH(val)               Hyperbolic Sine
    COSH(val)               Hyperbolic Cosine
    TANH(val)               Hyperbolic Tangens
    RAD(deg)                returns radian
    DEG(rad)                returns degrees
    LOG(val)                natural logarithm (base e)
    LOG10(val)              base 10 logarithm
    ROUND(val)              returns to the closest integer 
    FLOOR(val)              returns to the closest integer <= val
    CEILING(val)            returns to the closest integer >= val
    SQRT(val)               square root

    MAX(val, ...)           returns the biggest value
    MIN(val, ...)           returns the smallest value

    LERP(step, start, stop) calculates the lerp between start and stop. accepts also arrays.

    ARRAY(e1, e2, ...)      creates an array
    LENGTH(array)           returns the size of an array or 0 if it isn't

    VEC.NORMALIZE(array)    normalizes a numeric vector (array with three numeric values)
    VEC.LENGTH(array)       returns the length of a vector (array with three numeric values)

    IF(<condition>, <execute if true>, <execute if false>)

### Examples

for example if index has the value of 5:

    {'text[' + (index * 3) + ']'} returns 'text[15]'

but in this case (if value is 'text'):

    {if('text' == value, 1, 0)} returns 1

further examples:

    {sin(rad(angle))}

    {if(value == 10, value / 2, value ^ 2)}

if var1=1, var2=10, var3=9 then

    {max(var1, var2, var3, 7)} returns 10
