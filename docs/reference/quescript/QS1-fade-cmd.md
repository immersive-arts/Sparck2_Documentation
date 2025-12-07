# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;fade&gt;
&lt;fade name="(string)" timeout="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md))"&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <send>/address ramp {t1}</send>
    </anim>
    <wait countdown="2s"/>
    <fade name="simpleRamp" countdown="5s"/>

This example starts an animation with a duration of 5 seconds, waits for 2 seconds and then sends the animation a fadeout message.

### Attributes
* name = required. name of animation to fadeout. if the animation is a &lt;[while](QS1-while-cmd.md)&gt;, it will stop the loop immediately.
* fadeout =  the fadeout time of the animation. This overrides the fadeout-attibute of the &lt;[anim](QS1-anim-cmd.md)&gt; cmd.

### Child Commands
* None

### Explained
&lt;fade&gt; sends a 'fadeout' - message to all animations (&lt;[anim](QS1-anim-cmd.md)&gt; , &lt;[while](QS1-while-cmd.md)&gt;) with the indicated name inside this &lt;[que](QS1-que-cmd.md)&gt;

### Notice
When using [{expr}](QS1-Expressions.md) inside 'fadeout' the evaluated number is interpreted as milliseconds.