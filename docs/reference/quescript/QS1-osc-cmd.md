# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;osc&gt;
&lt;osc sendto="(string)"&gt;/address/pattern command arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/osc&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <osc>/address/pattern ramp {t1}</osc>
    </anim>
    <osc sendto="master">/animation/pattern executed</osc>
    <wait anim="simpleRamp"/>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* sendto = if specified, it will add the sendto string to the output list (see below). if not specified, the sendto string will be 'default'

### Child Commands
* None

### Explained
&lt;osc&gt; will create a Max-message that exits at the 'osc' - outlet of the [QueScript](../nodes/QueScript.md) node. With the above example it would be a list that looks like this:

    default /address/pattern ramp 0.
    master /animation/pattern executed

(if the above animation has just started). 

It is up to the implementing programmer to decide what to do with it. It is intended to send it to a 'route' - object to separate by the 'sendto'-values and then send via UDP it to different servers/ports, where '/address/pattern' is interpreted as the osc address-pattern.