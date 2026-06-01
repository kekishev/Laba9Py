# Laba 9
<p>The nineth laboratory work was done by Кекишев Андрей Сергеевич М80-106БВ-25</p>

## Description
<ol>
<li>
<b>__aiter__</b> method has been added in TaskQueue.
So, TaskQueue now supports both synchronous and asynchronous programming.<br>
Please, note that TaskQueue is only called in asynchronous context.
</li>
<li>JsonHandler, XmlHandler, LogicExample now work asynchronously.</li>
<li>
Added new interface <b>AsyncHandling</b> instead of expanding existed ones, 
what realizes interface segregation principle (ISP).
</li>
<li>
Dispatcher implements code extensibility idea.
</li>
<li>
New tests have been added. Some old tests have been fixed
</li>
</ol>