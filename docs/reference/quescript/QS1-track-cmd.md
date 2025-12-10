#[home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;[anim](QS1-anim-cmd.md)&gt;/&lt;track&gt;
&lt;track name="(string)" fadeto="float|[{expr}](QS1-Expressions.md))"&gt;

### Simple Example

```xml
    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <track name="t1" fadeto="2.">0. 1.</track>
        <send>/address ramp {t1}</send>
    </anim>
    <wait anim="simpleRamp"/>
```

### Attributes
* name = the name sets the variable name for expressions. assuming the above simple example: the name 't1' translates into two variables: 't1' for use inside the same &lt;anim&gt; node and 'simpleRamp.t1' for use inside the same &lt;que&gt;
* fadeto =  if the &lt;anim&gt; command has defined a fadeout attribute, it will use this value to target the fadeout for this variable.

### Content
A list of numbers or [{expr}](QS1-Expressions.md) that signifiy different key-values during the animation.

    <track name="t1" fadeto="2.">0. {expr} 10.</track>

this example defines three key values: 

* 0.
* [{expr}](QS1-Expressions.md) evaluated in realtime
* 10.5

the &lt;anim&gt; will create a linear interpolation between those values according to its normalized time. normalized time it is a factor of the &lt;anim&gt; duration.

if no &lt;keys&gt; object exists, &lt;anim&gt; will distribute the three key values evenly inside the duration. if the duration is 8s:

* value = 0. -> normalized time = 0.  -> at 0s  
* value = {expr} -> normalized time = 0.5 -> at 4s  
* value = 10.5 -> normalized time = 1.0 -> at 8s  

however, this distribution can be manually defined by the < [keys](QS1-keys-cmd.md) > cmd

### Explained
track is a variable that changes its value over time. the variable can be used by all [{expr}](QS1-Expressions.md)