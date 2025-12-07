# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;[anim](QS1-anim-cmd.md)&gt;/&lt;keys&gt;
&lt;keys timing="rel|abs"&gt;

### Simple Example

    <anim name="simpleRamp" duration="5s" fadeout="2s">
        <keys>0.8</keys>
        <track name="t1" fadeto="2.">0. {expr} 1.</track>
        <send>/address ramp {t1}</send>
    </anim>
    <wait anim="simpleRamp"/>

### Attributes
* timing =  if timing="rel", the content-values are interpreted as normalized times (between 0. and 1.).

### Parent Cmd
< [anim](QS1-anim-cmd.md) >
 
### Content
A list of numbers that define different key-times during the animation.

    <keys timing="rel">0.2</keys>
    <track name="t1">0 5. 10.</track>

in the above example &lt;track&gt; defines three key values: 

* 0.
* 5.
* 10.

if the &lt;track&gt; command has three values (n) specified, the &lt;keys&gt; command needs 1 (n-2) value(s), because the first and the last values are set:

value = 0.  -&gt; time = 0. (beginning of the animation)  
value = 5.  -&gt; time = set by &lt;keys&gt; (i.e. 0.2)  
value = 10. -&gt; time = 1. (end of the animation)  

if the duration of the &lt;anim&gt; was set to '10s' and the key command looks like : 

    <keys timing="rel">0.2</keys>

then the equivalent values for timing="abs" would look like this: 

    <keys timing="abs">2s</keys>

if you put an absolute time where quescript expects a relative time, you will get errormessages.

### Explained
-