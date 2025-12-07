# [QueScript](QS1-Introduction.md) / [Reference](QS1-Reference.md) / &lt;script&gt;
&lt;script&gt;  

### Simple Example

    <script>
        <var name="myVariable">345</var>
        <play name"Start"/>
        <que name="Start" loop="no">
        ....
        </que>
        <que name="Reset" loop="no">
        ....
        </que>
    </script>

### Attributes
* None

### Child Commands that have to appear in this sequence.
* &lt;[var](QS1-var-cmd.md)&gt;
* &lt;[stop](QS1-stop-cmd.md)&gt;
* &lt;[play](QS1-play-cmd.md)&gt;
* &lt;[que](QS1-que-cmd.md)&gt;

if this sequence is not adhered to, it will cause a parsing error.

### Explained
the &lt;script&gt; is the root element of the QueScript-file. 

the * &lt;[[stop|QS1-var-cmd]]&gt; node will cause to stop and remove all still running ques. if a name attribute is set, it will only stop the que with the specific name.

the * &lt;[[stop|QS1-var-cmd]]&gt; node will start playing the named que upon loading the script.

the &lt;[que](QS1-que-cmd.md)&gt; has to come after all the other child nodes.