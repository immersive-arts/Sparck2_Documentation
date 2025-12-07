# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;while&gt;
&lt;while name="(string)" start="[{expr}](QS1-Expressions.md)" repeat="[{expr}](QS1-Expressions.md)" step="[{expr}](QS1-Expressions.md))" &gt;

###Simple Example

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
* name = if name is set, &lt;while&gt; will sends an anim-message once the loop has exited (condition == false). this message can be caught by a &lt;wait anim="whileLoop"/&gt; cmd.
* init = if used, its [{expr}](QS1-Expressions.md) is evaluated first. Usefull to create a local variable inside the loop.
* condition =  required. its [{expr}](QS1-Expressions.md) has to be true (&gt;= 1) to go into the loop
* next = if used, its [{expr}](QS1-Expressions.md) is evaluated after each loop. Useful to increment a local variable inside the loop.

### Child Commands
* &lt;[expr](QS1-expr-cmd.md)&gt;
* &lt;[print](QS1-print-cmd.md)&gt;
* &lt;[send](QS1-send-cmd.md)&gt;
* &lt;[osc](QS1-osc-cmd.md)&gt;
* &lt;[out](QS1-out-cmd.md)&gt;
* &lt;[if](QS1-if-cmd.md)&gt;
* &lt;[play](QS1-play-cmd.md)&gt;
* &lt;[stop](QS1-stop-cmd.md)&gt;
* &lt;[shutdown](QS1-shutdown-cmd.md)&gt;
* &lt;[pause](QS1-pause-cmd.md)&gt;
* &lt;[resume](QS1-resume-cmd.md)&gt;
* &lt;[fade](QS1-fade-cmd.md)&gt;
* &lt;[trigger](QS1-trigger-cmd.md)&gt;
* &lt;[debugger](QS1-debugger-cmd.md)&gt;

### Explained
the &lt;while&gt; cmd defines an loop like structure for an animation and works like 'while' or 'for' in classical languages 

### Notice
* if a name-attribute is used, once the condition is false the node will send an anim-message to be caught by a &lt;wait anim="whileLoop"/&gt; node.
* the init-attribute's expression {:whilevar = 0} sets the variable 'whilevar' to 0. the **:** at the beginning of the variable name indicates that if the variable doesn't exist yet, the script will create the 'whilevar' variable in the local variable scope. the &lt;while&gt; node (like the &lt;[anim](QS1-anim-cmd.md)&gt; node) have a separate [[local variable scopes|QS1-Expr-Variables]] to the &lt;[que](QS1-que-cmd.md)&gt;. this way you can create variables that don't interfere with each other.