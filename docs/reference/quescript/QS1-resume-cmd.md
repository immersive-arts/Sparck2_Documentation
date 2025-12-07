# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;resume&gt;
&lt;resume name="(string)"/&gt;

### Simple Example

    <resume name="nextCue"/>

### Content
* None

### Attributes
* name = the name of the &lt;[que](QS1-que-cmd.md)&gt; to resume playing. If no name is set, all paused &lt;[que](QS1-que-cmd.md)&gt;s will resume playing.

### Child Commands
* None

### Explained
resumes playing another paused &lt;[que](QS1-que-cmd.md)&gt; inside the same script. If no name is specified, it will resume playing all paused ques. Using &lt;[pause](QS1-pause-cmd.md)&gt; lets ques be paused.