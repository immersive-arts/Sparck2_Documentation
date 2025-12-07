# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;timer&gt;
&lt;timer/&gt;

### Simple Example

    <timer/>
    <wait timer="1m:20s"/>

### Attributes
* None

### Child Commands
* None

### Explained
&lt;timer&gt; resets the parent &lt;[que](QS1-que-cmd.md)&gt;'s internal timer. The timer can be used by the &lt;[wait](QS1-wait-cmd.md)&gt;. 

It also creates an [{expr}](QS1-Expressions.md) Variable inside the que-domain called '$TIMER'. Its value is milliseconds since the last call of &lt;timer&gt;.
