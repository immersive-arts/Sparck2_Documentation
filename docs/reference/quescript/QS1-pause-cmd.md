# [QueScript](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;pause&gt;
&lt;pause name="(string)"/&gt;

### Simple Example

    <pause name="nextCue"/>

### Content
* None

### Attributes
* name = the name of the &lt;[que](QS1-que-cmd.md)&gt; to pause. If no name is set, all other &lt;[que](QS1-que-cmd.md)&gt;s will be paused.

### Child Commands
* None

### Explained
pauses another &lt;[que](QS1-que-cmd.md)&gt; inside the same script. If no name is specified, it will pause all running ques (except itself). Using &lt;[resume](QS1-resume-cmd.md)&gt; lets the paused ques playing again.