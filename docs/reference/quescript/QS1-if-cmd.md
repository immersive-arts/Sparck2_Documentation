# [QueScript](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;if&gt;
&lt;if true="[{expr}](QS1-Expressions.md)"&gt;

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
* true =  its [{expr}](QS1-Expressions.md) has to be true (&gt;= 1) to execute the content, otherwise &lt;else&gt; is called, if it exists
* false =  its [{expr}](QS1-Expressions.md) has to be false (0) to execute the content, otherwise &lt;else&gt; is called, if it exists

### Child Commands
* &lt;[[else|QS1-else-cmd]]&gt;
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
the &lt;if&gt; cmd works like 'if' in classical langauges 
