# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;wait&gt;

&lt;wait until="[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait while="[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait trigger="(string)"&gt;  
&lt;wait anim="(string)"&gt;  
&lt;wait faded="(string)"&gt;  
&lt;wait timer="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait countdown="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait hourglass="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait clock="[time](QS1-Timestring.md)|[{expr}](QS1-Expressions.md)"&gt;  
&lt;wait complex="and|or|not"&gt;  

### Simple Example

    <while name="whileLoop" init="{:whilevar = 0}" condition="{whilevar lt 100}" next="{whilevar = (whilevar + 1)}">
        <if true="{whilevar lt 50}">
            <print>inside while below 50: {whilevar}</print>
            <else>
                <print>inside while above 50: {whilevar}</print>
            </else>
        </if>
    </while>
    <wait anim="whileLoop"/>

### Attributes
* until = waits until the [{expr}](QS1-Expressions.md)-condition turns true.
* while = waits while the [{expr}](QS1-Expressions.md)-condition is true.
* timer = waits until the &lt;[timer](QS1-timer-cmd.md)&gt; has reached the specifed time. 1)
* watch = waits until the watch has reached the specifed time. 1)
* hourglass = waits until the watch has reached the specifed time inside this hour. 1)
* countdown = starts it own countdown with the specified length and waits until it has reached 0. 1)
* anim = waits until an 'anim' message with this name is sent. an 'anim' message are sent from &lt;[anim](QS1-anim-cmd.md)&gt; or &lt;[while](QS1-while-cmd.md)&gt;. It happens when the &lt;[anim](QS1-anim-cmd.md)&gt; finished its animation. If the &lt;[anim](QS1-anim-cmd.md)&gt; is looping (normal or palindrome), this will never happen for that animation. For &lt;[while](QS1-while-cmd.md)&gt; a name has to be set. the message is sent once the condition is FALSE.

* faded = waits until a 'faded' message with this name is sent.

a 'faded' message can only be sent by an &lt;[anim](QS1-anim-cmd.md)&gt; cmnd and happens once the animation has finished fading out.

* trigger = waits until a 'trigger' message with this pattern is sent.

A trigger message can be send by a &lt;[trigger](QS1-trigger-cmd.md)&gt; cmd or by a Max message to the QueScript object:

    trigger token1

A trigger message can also have multiple tokens:

    trigger token1 token2

where the following logic applies:

    <wait trigger="token1"/>        TRUE  IF 'trigger token1'
    <wait trigger="token1"/>        TRUE  IF 'trigger token1 token2'
    <wait trigger="token1 token2"/> TRUE  IF 'trigger token1 token2'
    <wait trigger="token2"/>        FALSE IF 'trigger token1 token2'
    <wait trigger="token1 token2"/> FALSE IF 'trigger token1'
    <wait trigger="token1 token2"/> FALSE IF 'trigger token2'

* complex = waits until the nested &lt;wait&gt; child commands are logicaly 'and'/'or'/'not'

Example:

     <wait complex="and">
         <wait trigger="triggername"/>
         <wait complex="or">
             <wait hourglass="1m"/>
             <wait timer="0m:10s"/>
         </wait>
     </wait>

This example waits until (( the minute finger of a clock is either past the first minute ) OR ( the timer has passed 10 seconds )) AND ( a trigger messgage 'triggername' was sent ).

&lt;wait&gt; cmnds that are nested inside a &lt;wait&gt;-complex behave a bit different. &lt;wait&gt;s are waiting for conditions that might be only true for one momemnt in time (like a 'trigger' or 'anim' - message). So their condition is only true for one bang. If you combine them in more complex conditions, then you would run into problems, because the different &lt;wait&gt; conditions happen at different moments in time. So inside a complex, if a &lt;wait&gt; has met its condition, it stays true.

### Child Commands
* &lt;wait&gt;

### Explained
the &lt;wait&gt; cmd requires only one of the above attributes. It halts the further execution of the script until its set condition has occured. Meanwhile, animation command like &lt;[anim](QS1-anim-cmd.md)&gt; or &lt;[while](QS1-while-cmd.md)&gt; will continue to run according to their settings.

### Notice 1)
When using [{expr}](QS1-Expressions.md) inside 'timer', 'watch', 'hourglass' and 'countdown', the evaluated number is interpreted as milliseconds.