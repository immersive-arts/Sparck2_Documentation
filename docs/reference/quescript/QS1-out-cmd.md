# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;out&gt;
&lt;out&gt;command arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/out&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <out>command ramp {t1}</out>
    </anim>
    <wait anim="simpleRamp"/>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
Like all messages, &lt;out&gt; will create a Max-message that exits at the left outlet of the QueScript Max-object. With the above example it would be a list that looks like this:

    out command ramp 0.

(if the above animation has just started). 

It is up to the implementing porgrammer to decide what to do with it. It is intended to send it to a 'route' - object to separate the 'out' from the other messages and then to do what ever the programmers intentions are.