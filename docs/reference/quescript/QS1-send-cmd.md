# [QueScript](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;send&gt;
&lt;send&gt;/address command arg1 arg2 [{expr}](QS1-Expressions.md)&lt;/send&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1">0. 1.</track>
        <send>/address ramp {t1}</send>
    </anim>
    <wait anim="simpleRamp"/>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
Like all messages, &lt;send&gt; will create a Max-message that exits at the left outlet of the QueScript Max-object. With the above example it would be a list that looks like this:

    send /address ramp 0.

(if the above animation has just started). 

It is up to the implementing programmer to decide what to do with it. It is intended to send it to a 'route' - object in order to separate it from the other messsages and then to pass the leftover ('/address ramp 0.') to a little javaScript:

    inlets = 1;
    function anything(){
        messnamed(messagename, arrayfromargs(arguments));
    }
where '/address' is interpreted as the reciever address for a Max receive-object.