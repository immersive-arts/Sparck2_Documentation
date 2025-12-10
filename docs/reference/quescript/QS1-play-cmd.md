# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;play&gt;
&lt;play name="(string)"/&gt;

### Simple Example

```xml
    <play name="nextCue"/>
```

### Content
* None

### Attributes
* name = required. the name of the &lt;[que](QS1-que-cmd.md)&gt; to execute playing. 

### Child Commands
* None

### Explained
Plays another &lt;[que](QS1-que-cmd.md)&gt; inside the same script.

```xml
    <que name="Start" loop="no">
        <play name="Reset"/>
        <wait trigger="resetDone"/>
        <print>Reseted. Ready for action</print>
    </que>
    <que name="Reset" loop="no">
        <print>Executing Reset</print>
        <trigger>resetDone</trigger>
    </que>
```

When &lt;[que](QS1-que-cmd.md)&gt; 'Start' is played, first thing it will start playing &lt;[que](QS1-que-cmd.md)&gt; 'Reset' and &lt;[wait](QS1-wait-cmd.md)&gt; for a trigger called 'resetDone'. When &lt;[que](QS1-que-cmd.md)&gt; 'Reset' plays, it first &lt;[print](QS1-print-cmd.md)&gt;s out the message 'Executing Reset' and then sends a &lt;trigger&gt;-message 'resetDone'. Which the &lt;[wait](QS1-wait-cmd.md)&gt; cmd inside 'Start' will pickup and carry on with &lt;[print](QS1-print-cmd.md)&gt;ing 'Reseted. Ready for action'.