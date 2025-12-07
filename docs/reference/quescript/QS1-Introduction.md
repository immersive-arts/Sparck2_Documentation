# QueScript

QueScript is a Java-based Max External for writing animation scripts.

It has a rich feature set of [commands](QS1-Reference.md) that allow a unique way of writing complex cue-triggered animations that can be easily implemented into existing max patches.

Lets have a look at a simple example.

QueScript is XML based, and you can use the internal Max-Text editor or any Suitable editor of your choice (mine is [TextWrangler](http://www.barebones.com/products/textwrangler/)).

    <script>
        <que name="myQue">
            <timer>
            <send>/address list with strings and numbers 0 2.45 56</send>
            <wait timer="5s"/>
            <print>timer has passed</print>
        </que>
    </script>

when playing 'myQue', QueScript (from now on called 'QS') will start a timer and send a message to the leftmost outlet:

`send /address list with strings and numbers 0 2.45 56`

then it waits until 5 seconds of the &lt;[timer](QS1-timer-cmd.md)&gt; call have passed and then sends another message to the left outlet:

`print timer has passed`

its up to you what you want to do with those message-lists, but with a simple 'route' object you can use the &lt;[send](QS1-send-cmd.md)&gt; for Max internal send/receive objects and &lt;[print](QS1-print-cmd.md)&gt; for printing to the console. there are even more [[messages|QS1-Reference#messages]] to choose from.

However, QS doesnt stop here. There are animation commands that allow you to create simple timelines and loops that can run concurrently. Lets have a look at a simple use of the < [anim](QS1-anim-cmd.md) > command:

    <script>
        <que name="my2ndQue">
            <anim name="simpleRamp" duration="5s" fadeout="2s">
                 <track name="t1">0. 1.</track>
                 <send>/address ramp {t1}</send>
            </anim>
            <wait anim="simpleRamp"/>
            <print>animation is fading out</print>
        </que>
    </script>

when playing que "my2ndQue", QS will start an animation with a duration of 5 seconds. it has a child-cmd called  &lt;[track](QS1-track-cmd.md)&gt; in which two values, 0. and 1. are set. this means &lt;[track](QS1-track-cmd.md)&gt; will create a variable called 't1' (the name of the track) and change its value from 0. to 1. within 5 seconds. the other childe-cmd called &lt;[send](QS1-send-cmd.md)&gt; creates a send message with the value of that variable.

Since the QueScript object requires a bang-message for each iteration through its internal time, you would usually attach a metro- or qmetro-object to the QS1-object. If the qmetro-object is giving a bang each second, you would get the folloing output from the left outlet:

`send /address ramp 0.`  
`send /address ramp 0.2`  
`send /address ramp 0.4`  
`send /address ramp 0.6`  
`send /address ramp 0.8`  
`send /address ramp 1`  

after the &lt;[anim](QS1-anim-cmd.md)&gt; cmd comes again a &lt;[wait](QS1-wait-cmd.md)&gt; cmd, but this time it is waiting for a message from the &lt;[anim](QS1-anim-cmd.md)&gt; cmd: As soon as the &lt;[anim](QS1-anim-cmd.md)&gt; cmd has finished it animation, it will send (internally) an anim-message which &lt;wait anim="simpleRamp"&gt; has been wating for. This allows you to keep your script waiting until certain animations have finished before it carries on.

the next is another message from the left inlet:

`print animation is fading out`

and

`send /address ramp 0.5`  
`send /address ramp 0.`

the folloing is happening here. When a Que reaches its end, it sends all its animations a 'shutdown' message (something you can do with the &lt;[shutdown](QS1-shutdown-cmd.md)&gt; cmd, too). Since we gave a 'fadeout' time, it will try to gracefully fadeout the animation inside the provided timespan to the initial value (0.). If you dont like this behaviour, simply dont give a 'fadeout' time.

Obviously you can create as many &lt;[track](QS1-track-cmd.md)&gt; commands inside <anim> as you wish, as long as you give them different naming, and inside the &lt;[track](QS1-track-cmd.md)&gt; cmd you can use as many values (not only two) as want. and you can send as many messages as you want.

Lets have a look at one last example:

    <script>
        <que name="my2ndQue">
            <anim name="simpleRamp" duration="5s" fadeout="2s">
                 <track name="t1">0. 1.</track>
                 <send>/address ramp {t1}</send>
            </anim>
            <anim name="simpleLoop" duration="5s" loop="palindrome">
                 <track name="t1">0. 1. 0.</track>
                 <send>/address palindrome {t1} {simpleRamp.t1}</send>
            </anim>
            <wait trigger="keepGoing"/>
            <print>animation is fading out</print>
        </que>
    </script>

This script will start two animations at the same time. the one called 'simpleRamp' will create the same ramp - messages as we already have seen in the last example. the one called 'simpleLoop' will create an never ending palindrome loop following the tree values 0. to 1. to 0. and then 1. and 0. and then 1. and 0. etc.

Notice the {simpleRamp.t1} inside the <send> cmd. this means it actually references inside of 'simpleLoop' to the animated variable 't1' of the 'simpleRamp'. (Find here more about [[variables|QS1-expr-variables]])

this animation will happyily carry on until a 'trigger' message reaches the que. trigger messages can be generated by a user with a Max 'trigger' message sent to the QS1-object or by the script through the &lt;[trigger](QS1-trigger-cmd.md)&gt; cmd.

What I failed to mention so far: it is actually possible to run mutiple Ques in parallel. And each Que can &lt;[play](QS1-play-cmd.md)&gt;, &lt;[pause](QS1-pause-cmd.md)&gt;, &lt;[resume](QS1-resume-cmd.md)&gt;, &lt;[stop](QS1-stop-cmd.md)&gt; or &lt;[trigger](QS1-trigger-cmd.md)&gt; other ques inside the same script at your leasure.

What I also failed to mention is the power of the &lt;[{expressions}](QS1-expressions.md)&gt;. All of the values (numbers or times except attributes that require strings) can be expressed with an {expression}. But that is another story.
