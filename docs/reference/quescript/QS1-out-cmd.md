# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;out&gt;
&lt;out&gt;command arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/out&gt;

### Simple Example

```xml
    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <out>command ramp {t1}</out>
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
&lt;out&gt; will create a Max-message that exits at the left outlet of the 'out' - outlet of the [QueScript](../nodes/QueScript.md) node. With the above example it would be a list that looks like this:

    out command ramp 0.

(if the above animation has just started). 
