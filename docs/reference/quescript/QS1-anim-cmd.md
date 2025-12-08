# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;anim&gt;
&lt;anim name="(string)" duration="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md))" fadeout="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md))" loop="no|normal|palindrome"&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <send>/address ramp {t1}</send>
    </anim>
    <wait anim="simpleRamp"/>

### Attributes
* name = required. name of animation
* duration = the duration of the animation. [^1]
* fadeout =  the fadeout time of the animation. [^1]
* loop = loop mode: no|normal|palindrome

### Child Commands
* &lt;[track](QS1-track-cmd.md)&gt;
* &lt;[keys](QS1-keys-cmd.md)&gt;
* &lt;[expr](QS1-expr-cmd.md)&gt;
* &lt;[print](QS1-print-cmd.md)&gt;
* &lt;[send](QS1-send-cmd.md)&gt;
* &lt;[osc](QS1-osc-cmd.md)&gt;
* &lt;[out](QS1-out-cmd.md)&gt;
* &lt;[if](QS1-if-cmd.md)&gt;
* &lt;[debugger](QS1-debugger-cmd.md)&gt;

### Explained
&lt;anim&gt; creates key-based animations. It needs at least one &lt;[track](QS1-track-cmd.md)&gt; cmnd and one message (&lt;[print](QS1-print-cmd.md)&gt;, &lt;[send](QS1-send-cmd.md)&gt;, &lt;[osc](QS1-osc-cmd.md)&gt;, &lt;[out](QS1-out-cmd.md)&gt;). &lt;[track](QS1-track-cmd.md)&gt; defines a set of simple ramps that are interpolated during the specified duration of the animation. with &lt;[keys](QS1-keys-cmd.md)&gt;[^2] it is possible to adjust the timing of those ramps.

if &lt;anim&gt; has no loop and has reached its target, it will send an internal anim-message with its name, which can be picked up by a &lt;[wait](QS1-wait-cmd.md)&gt; cmnd. this way it is possible to let the quescript wait until an anim has finished until it continues.

if &lt;anim&gt; is fading out and has reached its end, it will send an internal faded-message with its name, which can be picked up by a &lt;[wait](QS1-wait-cmd.md)&gt; cmnd. this way it is possible to let the quescript wait until an anim has finished fading out until it continues.

[^1]: :man_raising_hand: When using [{expr}](QS1-Expressions.md) inside 'duration' and 'fadeout', the evaluated number is interpreted as milliseconds.

[^2]: :man_raising_hand:Only maximal one &lt;[keys](QS1-keys-cmd.md)&gt; cmnd is allowed and applies to all &lt;[track](QS1-track-cmd.md)&gt; cmnds. This means the number of &lt;[track](QS1-track-cmd.md)&gt; values must be n+2 of the &lt;[keys](QS1-keys-cmd.md)&gt; values.
