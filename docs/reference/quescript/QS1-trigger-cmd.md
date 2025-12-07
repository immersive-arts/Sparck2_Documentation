# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;trigger&gt;
&lt;trigger&gt;(string) [{expr}](QS1-Expressions.md)&lt;/trigger&gt;

### Simple Example

    <trigger>nextCue</trigger>

### Content
Any List of Strings, numbers and [{expr}](QS1-Expressions.md)

### Attributes
* None

### Child Commands
* None

### Explained
The main difference to the other messages is it creates also an internal 'trigger' message that is send to all the currently playing ques of this script. this allows to trigger &lt;[wait](QS1-wait-cmd.md)&gt; cmds in other ques. Example:

    <que name="Start" loop="no">
        <play name="Reset"/>
        <wait trigger="resetDone"/>
        <print>Reseted. Ready for action</print>
    </que>
    <que name="Reset" loop="no">
        <print>Executing Reset</print>
        <trigger>resetDone</trigger>
    </que>

When &lt;[que](QS1-que-cmd.md)&gt; 'Start' is played, first thing it does is start playing &lt;[que](QS1-que-cmd.md)&gt; 'Reset' and &lt;[wait](QS1-wait-cmd.md)&gt; for a trigger called 'resetDone'. When &lt;[que](QS1-que-cmd.md)&gt; 'Reset' plays, it first &lt;[print](QS1-print-cmd.md)&gt;s out the message `Executing Reset` and then sends a &lt;trigger&gt;-message 'resetDone'. Which the &lt;[wait](QS1-wait-cmd.md)&gt; cmd inside 'Start' will pickup and carry on with &lt;[print](QS1-print-cmd.md)&gt;ing `Reseted. Ready for action`.

Like all messages, &lt;trigger&gt; will create a Max-message that exits at the left outlet of the QueScript Max-object. With the above example it would be a list that looks like this:

    trigger nextCue

It is up to the implementing programmer to decide what to do with it. It is intended to send it to a 'route' - object in order to separate it from the other messsages and could be used to trigger other QueScript-objects.