<h1>Laba 6</h1>
<p>The sixth laboratory work was done by Кекишев Андрей Сергеевич М80-106БВ-25</p>

<h3>Description</h3>
<p>
Two Protocol interfaces were realized: "Executable" and "TaskHandling".
</p>

The crucial thing to know is that:
<ol>
<li>JsonHandler implements all interfaces (Executable and TaskHandling).</li>
<li>XmlHandler implements only TaskHandling.</li>
<li>Task generates in TaskGenerator</li>
<li>Example logic is inside LogicExample class</li>
<li>Type annotations, Protocol, @runtime_checkable, isinstance() are used.</li>
</ol>