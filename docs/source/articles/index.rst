Articles
============

*The first place to look when you want to read something worth reading about Python.*

This is a curated, `community-voted <https://t.me/python_belgrade>`_ section of articles from across the Python ecosystem. It's not just an aggregator however, think of it like a high-signal place to keep yourself informed about Python and its ecosystem.

Links to past years' archives can be found at the bottom of the page.

----

{% for article in articles["2026"] %}

{% set heading = "`" + article.title + " ↗ <" + article.url + ">`_" %}
- .. rubric:: {{ heading }}

  
  by `{{ article.author }} ↗ <{{ article.authorUrl }}>`_

  .. image:: {{ article.image }}
     :height: 10em

  {{ article.description }}


{% endfor %}
