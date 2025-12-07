# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;debugger&gt;

### Simple Example

    <debugger scope="que">

### Attributes
* scope = (script|que|local) specifies which [[variable scope|QS1-Expr-Variables]] it should print out to the console. 
* name = gives the debug message an identifier.

### Child Commands
* None

### Explained
&lt;debugger&gt; allows in runtime to see all the used Variables, sorted by scope. It only works if the Max message `debug 1` is sent to the QueScript object.
