Meetups
=======

Hi, you can browse info about previous meetups here.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   {% for meetup in meetups %}
   meetup_{{ meetup.id }}
   {% endfor %}
