# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;stop&gt;
&lt;stop name="(string)"/&gt;

### Simple Example

    <stop name="nextCue"/>

### Content
* None

### Attributes
* name = the name of the &lt;[que](QS1-que-cmd.md)&gt; to stop playing. If no name is set, all other &lt;[que](QS1-que-cmd.md)&gt;s will be stopped.

### Child Commands
* None

### Explained
Stops another &lt;[que](QS1-que-cmd.md)&gt; inside the same script. If no name is specified, it will stop all running ques. In comparison to &lt;[shutdown](QS1-shutdown-cmd.md)&gt;, it will stop the ques immediately without any gracefull fadeouts.