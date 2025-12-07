# [home](QS1-Introduction.md) / [reference](QS1-Reference.md) / &lt;que&gt;
&lt;que name="(string)" loop="no|normal|palindrome"&gt;

### Simple Example

    <que name="Start" loop="no">
        <play name="Reset"/>
        <wait trigger="resetDone"/>
        <print>Reseted. Ready for action</print>
    </que>
    <que name="Reset" loop="no">
        <print>Executing Reset</print>
        <trigger>resetDone</trigger>
    </que>

### Attributes
* name = required. name of que
* loop = loop mode: no|normal

If the no loop is set, the &lt;que&gt; simply shuts itself down once the script reaches its end. Shuting down the &lt;que&gt; means, it will allow all &lt;[anim](QS1-anim-cmd.md)&gt;'s that are still running to start fadeout until they are finished and then stop. If the loop is set to normal, the &lt;que&gt; will stop all still running animations (&lt;[anim](QS1-anim-cmd.md)&gt;, &lt;[while](QS1-while-cmd.md)&gt;) on the spot and start from the top again.

### Child Commands
* &lt;[var](QS1-var-cmd.md)&gt;
* &lt;[anim](QS1-anim-cmd.md)&gt;
* &lt;[while](QS1-while-cmd.md)&gt;
* &lt;[expr](QS1-expr-cmd.md)&gt;
* &lt;[print](QS1-print-cmd.md)&gt;
* &lt;[send](QS1-send-cmd.md)&gt;
* &lt;[osc](QS1-osc-cmd.md)&gt;
* &lt;[out](QS1-out-cmd.md)&gt;
* &lt;[if](QS1-if-cmd.md)&gt;
* &lt;[fade](QS1-fade-cmd.md)&gt;
* &lt;[play](QS1-play-cmd.md)&gt;
* &lt;[stop](QS1-stop-cmd.md)&gt;
* &lt;[shutdown](QS1-shutdown-cmd.md)&gt;
* &lt;[pause](QS1-pause-cmd.md)&gt;
* &lt;[resume](QS1-resume-cmd.md)&gt;
* &lt;[debugger](QS1-debugger-cmd.md)&gt;
* &lt;[timer](QS1-timer-cmd.md)&gt;

### Explained
&lt;que&gt; defines the core structure of QueScript. &lt;que&gt;'s are executed with a Max message to the QueScript object like `play 'queName'` or from within another &lt;que&gt; with &lt;[play](QS1-play-cmd.md)&gt;.

The messages `pause 'queName'` and `resume 'queName'` will pause and resume a specific que. This also can be achieved with &lt;[pause](QS1-pause-cmd.md)&gt; and &lt;[resume](QS1-resume-cmd.md)&gt; from within another &lt;que&gt;.

If the `autostart 1` message is sent to the QueScript objects before a script is loaded, QueScript will play the first &lt;que&gt; inside the &lt;script&gt; upon finishing loading.

If a new script is loaded and a &lt;que&gt; is still playing, it will keep on running until it either finishes or is stopped by a &lt;[stop](QS1-stop-cmd.md)&gt; or &lt;[shutdown](QS1-shutdown-cmd.md)&gt; command.

