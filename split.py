from bs4 import BeautifulSoup


def split_html_message(html_message, max_len):
    soup = BeautifulSoup(html_message, 'html.parser')
    fragments = []
    current_fragment = ''
    current_len = 0

    def append_fragment(fragment):
        if fragment.strip():  # Exclude empty fragments
            fragments.append(fragment)

    for element in soup.descendants:
        if isinstance(element, str):  # Text node
            while element:
                remaining_len = max_len - current_len
                if len(element) <= remaining_len:
                    current_fragment += element
                    current_len += len(element)
                    element = ''
                else:
                    current_fragment += element[:remaining_len]
                    append_fragment(current_fragment)
                    current_fragment = ''
                    current_len = 0
                    element = element[remaining_len:]
        else:  # Tag
            tag_html = str(element)
            if len(current_fragment) + len(tag_html) <= max_len:
                current_fragment += tag_html
                current_len += len(tag_html)
            else:
                append_fragment(current_fragment)
                current_fragment = tag_html
                current_len = len(tag_html)

    append_fragment(current_fragment)  # Append remaining fragment

    return fragments


source_html = """
    <strong>🕒 Some tasks are missing worklogs!</strong>
<mention id="U1024">Justin	Kirvin</mention>
Here is the list of tasks that have been in status without worklogs for more than <strong>1h</strong> :arrow_down:

<a href="tg://user?id=3485734953">Talbert Gannaway</a>
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12634"><code>ABC-12634</code></a> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

<strong>Done</strong>
<i>
<a href="https://mockdata.atlassian.net/browse/ABC-12508"><code>ABC-12508</code></a> Vestibulum pellentesque ullamcorper sapien sed venenatis.
<a href="https://mockdata.atlassian.net/browse/ABC-12587"><code>ABC-12587</code></a> Integer et erat mollis, tempor sem a, fringilla est.
</i>

<a href="tg://user?id=604521009">Jilly Paolillo</a>
<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12255"><code>ABC-12255</code></a> Vestibulum ante ipsum primis in faucibus orci luctus et…
<a href="https://mockdata.atlassian.net/browse/ABC-12365"><code>ABC-12365</code></a> Nunc molestie enim augue, non vulputate urna feugiat quis

Paul Gallaher
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12166"><code>ABC-12166</code></a> Integer aliquet, dui eget vestibulum hendrerit, nulla augue pharetra sem
<a href="https://mockdata.atlassian.net/browse/ABC-12464"><code>ABC-12464</code></a> Suspendisse libero neque, commodo in condimentum in

<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12346"><code>ABC-12346</code></a> Maecenas pretium tellus sed turpis interdum cursus.


Mara Crone
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-11571"><code>ABC-11571</code></a> Cras sodales dignissim nibh in placerat.
<a href="https://mockdata.atlassian.net/browse/ABC-12612"><code>ABC-12612</code></a> Cras vel orci justo.

<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-11004"><code>ABC-11004</code></a> Mauris eleifend imperdiet neque.
<a href="https://mockdata.atlassian.net/browse/ABC-12390"><code>ABC-12390</code></a> Cras condimentum congue lorem.
<a href="https://mockdata.atlassian.net/browse/ABC-12541"><code>ABC-12541</code></a> Ut efficitur ligula pretium ac.

<a href="tg://user?id=1968271026">Talbert Gannaway</a>
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-11916"><code>ABC-11916</code></a> Sed at lacus porttitor, vulputate ante sed.

<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12186"><code>ABC-12186</code></a> Faucibus dui.
<a href="https://mockdata.atlassian.net/browse/ABC-12384"><code>ABC-12384</code></a> In augue lacus, volutpat porta erat non…
<a href="https://mockdata.atlassian.net/browse/ABC-12406"><code>ABC-12406</code></a> Aliquet mattis felis.
<a href="https://mockdata.atlassian.net/browse/ABC-12419"><code>ABC-12419</code></a> Nam non neque diam.
<a href="https://mockdata.atlassian.net/browse/ABC-12509"><code>ABC-12509</code></a> Donec sed sodales metus.
<a href="https://mockdata.atlassian.net/browse/ABC-12535"><code>ABC-12535</code></a> Aliquam sagittis bibendum tellus, sed feugiat lacus mattis eu.

<a href="tg://user?id=1697777562">Konstantin Babushkin</a>
<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12427"><code>ABC-12427</code></a> Fusce cursus euismod ligula nec ullamcorper.
<a href="https://mockdata.atlassian.net/browse/ABC-12452"><code>ABC-12452</code></a> Nam vulputate feugiat.
<a href="https://mockdata.atlassian.net/browse/ABC-12513"><code>ABC-12513</code></a> Sem, eu cursus neque interdum ac.
<a href="https://mockdata.atlassian.net/browse/ABC-12580"><code>ABC-12580</code></a> Nulla sodales libero eu lectus gravida varius.

Christan Van der Kruys
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12503"><code>ABC-12503</code></a> In sem libero, lobortis eu posuere quis, iaculis sed.

<strong>Done</strong>
<span>
<p>test</p>
<a href="https://mockdata.atlassian.net/browse/ABC-11872"><code>ABC-11872</code></a> Etiam cursus nisi eget tortor feugiat.
<a href="https://mockdata.atlassian.net/browse/ABC-12129"><code>ABC-12129</code></a> Non congue tortor cursus.
<div>
<a href="https://mockdata.atlassian.net/browse/ABC-12354"><code>ABC-12354</code></a> Ut finibus urna sed lorem elementum.
<a href="https://mockdata.atlassian.net/browse/ABC-12398"><code>ABC-12398</code></a> Eget tristique magna vulputate.
<a href="https://mockdata.atlassian.net/browse/ABC-12455"><code>ABC-12455</code></a> Sed a orci at turpis commodo semper quis vitae erat.
<a href="https://mockdata.atlassian.net/browse/ABC-12522"><code>ABC-12522</code></a> Quis purus et augue varius egestas
</div>
<a href="https://mockdata.atlassian.net/browse/ABC-12538"><code>ABC-12538</code></a> Aliquam ac sollicitudin neque.
</span>
Millie Isaksson
<strong>In progress</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12062"><code>ABC-12062</code></a> Duis rhoncus venenatis risus in mollis.

<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-12385"><code>ABC-12385</code></a> Maecenas vitae maximus leo.
<a href="https://mockdata.atlassian.net/browse/ABC-12472"><code>ABC-12472</code></a> Aliquam interdum mauris ut urna semper elementum.

Manuel	Stanney
<strong>Done</strong>
<a href="https://mockdata.atlassian.net/browse/ABC-1005"><code>ABC-1005</code></a> In ultrices lobortis mauris in interdum.
<a href="https://mockdata.atlassian.net/browse/ABC-976"><code>ABC-976</code></a> Mauris imperdiet non lorem eget congue.
<a href="https://mockdata.atlassian.net/browse/ABC-12408"><code>ABC-12408</code></a> Nullam tincidunt vulputate nibh a placerat.

"""

max_len = 4096  # Example maximum length
fragments = split_html_message(source_html, max_len)
for fragment in fragments:
    print("Fragment:", fragment)
    print("===")  # Separating fragments for clarity
