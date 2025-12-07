# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;print&gt;
&lt;print&gt;message arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/print&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <print>message ramp {t1}</print>
    </anim>
    <wait anim="simpleRamp"/>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
Like all messages, &lt;print&gt; will create a Max-message that exits at the left outlet of the QueScript Max-object. With the above example it would be a list that looks like this:

    print message ramp 0.

(if the above animation has just started). 

It is up to the implementing programmer to decide what to do with it. It is intended to send it to a 'route' - object and then to pass the leftover ('message ramp 0.') to a Max print-object.