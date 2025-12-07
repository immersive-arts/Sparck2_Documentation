# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;shutdown&gt;
&lt;shutdown name="(string)"/&gt;

### Simple Example

    <shutdown name="nextCue"/>

### Content
* None

### Attributes
* name = the name of the &lt;[que](QS1-que-cmd.md)&gt; to shutdown. If no name is set, all other &lt;[que](QS1-que-cmd.md)&gt;s will be shutdown.

### Child Commands
* None

### Explained
Shutdown another &lt;[que](QS1-que-cmd.md)&gt; inside the same script. If no name is specified, it will shutdown all running ques. In comparison to &lt;[stop](QS1-stop-cmd.md)&gt;, this will allow the running animations inside the que's to fadeout gracefully.