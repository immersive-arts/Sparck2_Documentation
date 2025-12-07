# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;[if](QS1-if-cmd.md)&gt;/&lt;else&gt;
&lt;else&gt;

### Simple Example

    <while name="whileLoop" start="{whilevar = 0}" repeat="{whilevar lt 100}" step="{whilevar = (whilevar + 1)}">
        <if true="{whilevar lt 50}">
            <print>inside while below 50: {whilevar}</print>
            <else>
                <print>inside while above 50: {whilevar}</print>
            </else>
        </if>
    </while>
    <wait anim="whileLoop"/>

### Attributes
* None

### Parent Command
* &lt;[if](QS1-if-cmd.md)&gt;

### Child Commands
* &lt;[expr](QS1-expr-cmd.md)&gt;
* &lt;[print](QS1-print-cmd.md)&gt;
* &lt;[send](QS1-send-cmd.md)&gt;
* &lt;[osc](QS1-osc-cmd.md)&gt;
* &lt;[out](QS1-out-cmd.md)&gt;
* &lt;[trigger](QS1-trigger-cmd.md)&gt;
* &lt;[if](QS1-if-cmd.md)&gt;
* &lt;[while](QS1-while-cmd.md)&gt;
* &lt;[anim](QS1-anim-cmd.md)&gt;
* &lt;[play](QS1-play-cmd.md)&gt;
* &lt;[stop](QS1-stop-cmd.md)&gt;
* &lt;[pause](QS1-pause-cmd.md)&gt;
* &lt;[resume](QS1-resume-cmd.md)&gt;
* &lt;[shutdown](QS1-shutdown-cmd.md)&gt;
* &lt;[debugger](QS1-debugger-cmd.md)&gt;


### Explained
the &lt;else&gt; cmd works like 'else' in classical langauges 
