# [QueScript](QS1-Introduction.md) / [reference](QS1-Reference.md) / [{expressions}](QS1-expressions.md) / Usage

this is a complete list where inside the quescript [{expressions}](QS1-expressions.md) can be used

    <anim name="anim1" duration="{expr}" fadeout="{expr}">
        <track name="track1" fadeto="{expr}">0. {expr}</track>
        <send>/sendadress command {expr} {expr}</send>
    </anim>
&lt;[anim](QS1-anim-cmd.md)&gt;  
&lt;[track](QS1-track-cmd.md)&gt;

    <expr>{expr}</expr>
&lt;[expr](QS1-expr-cmd.md)&gt;  

    <wait until="{expr}"/>
    <wait while="{expr}"/>
&lt;[wait](QS1-wait-cmd.md)&gt;  

    <print>{expr}</print>
&lt;[print](QS1-print-cmd.md)&gt;  

    <send>/sendadress {expr}</send>
&lt;[send](QS1-send-cmd.md)&gt;  

    <out>{expr}</out>
&lt;[out](QS1-out-cmd.md)&gt;  

    <osc>{expr}</osc>
&lt;[osc](QS1-osc-cmd.md)&gt;  

    <trigger>{expr} {expr}</trigger>
&lt;[trigger](QS1-trigger-cmd.md)&gt;  

    <while init="{expr}" condition="{expr}" next="{expr}">
    </while>
&lt;[while](QS1-while-cmd.md)&gt;  

    <if true={expr}>
        <else>
        </else>
    </if>
&lt;[if](QS1-if-cmd.md)&gt;  

###Usage Examples

    <expr>{global = if(global==0, 45, global)}</expr>
Allows to execute expressions. Since it is also possible to assign variables inside expressions, more complex algorithmic constructions are possible.

    <anim name="anim1" duration="10s" fadeout="2s">
        <track name="t1" fadeto="{log(global)}">0. {global}</track>

&lt;[track](QS1-track-cmd.md)&gt; in combination with &lt;[anim](QS1-anim-cmd.md)&gt; creates two variables that changes its value over time, from the first set value (0) to the last set value ({global}) in 10 seconds.

the name of the first variable is t1 and can only be used inside the &lt;[anim](QS1-anim-cmd.md)&gt; command.
the name of the second variable is anim1.t1 and can be used inside the &lt;[que](QS1-que-cmd.md)&gt; command (as soon as the &lt;[anim](QS1-anim-cmd.md)&gt; node was executed)

        <send>/sendadress command {t1} {anim1.t1}</send>

this &lt;[send](QS1-send-cmd.md)&gt; command references the created values and creates a send message.

    </anim>

    <wait until="{anim1.t1 > (var_1 / 2)}"/>

the &lt;[wait](QS1-wait-cmd.md)&gt; command waits until the value of the variable anim1.t1 is greater than half of val_1. If this &lt;[wait](QS1-wait-cmd.md)&gt; command was right after the &lt;[anim](QS1-anim-cmd.md)&gt; command, it would wait for 5s before the script carries on, because it takes the &lt;[anim](QS1-anim-cmd.md)&gt; command 10 seconds to reach var_1 for the variable anim1.t1.
