# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;print&gt;
&lt;print&gt;message arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/print&gt;

### Simple Example

```xml
    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <print>message ramp {t1}</print>
    </anim>
    <wait anim="simpleRamp"/>
```

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
Like all messages, &lt;print&gt; will create a Max-message that is printed directly to the Max Console. With the above example it would be a line in the console that looks like this:

    QueScript * message ramp 0.

(if the above animation has just started). 
