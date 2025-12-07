# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;var&gt;

**&lt;var&gt; has ALWAYS to be the first node inside a &lt;script&gt; or &lt;que&gt; node**

### Simple Example

assign an array to a variable:

    <var name="variablename">{ARRAY(0,0,0)}</var>

reference a expression to a variable:

    <var name="variablename">{-> ARRAY(COS(alpha),sin(alpha),2)}</var>


### Attributes
* name = name of a variable inside the scope of the node

### Explained
&lt;var&gt; instantiates a variable and either
  * evaluates the [{expr}](QS1-Expressions.md) and sets the result as its value
  * sets the reference to the [{expr}](QS1-Expressions.md) as its value

setting a reference to a variable will execute the expression each time the variable is used further along the code and returns the result of its evaluation. In a sense it is a definition of a function call that can be referenced by the variable.
