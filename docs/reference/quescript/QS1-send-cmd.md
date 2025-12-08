# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;send&gt;
&lt;send&gt;/address command arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/send&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <send>address ramp {t1}</send>
    </anim>
    <wait anim="simpleRamp"/>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
&lt;send&gt; will send a Max-message to any [[receive](https://docs.cycling74.com/reference/gen_common_receive/)] object within the max environment. With the above example it would be a list that looks like this:

    ramp 0.

(if the above animation has just started). 
