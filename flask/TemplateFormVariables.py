{% extends "base.html" %}
{% block content %}
  <h1>{{ template_recipe | title }}</h1>
  {% if template_description %}
    <p>{{ template_description }}</p>
  {%else%}
    <p>A {{ template_recipe }} recipe.</p>
  {% endif %}
  <h3>Ingredients - {{ template_ingredients | length}}</h3>
  <ul>
  {% for ingredient in template_ingredients %}
      <li>{{ ingredient }}</li>
  {% endfor %}
  </ul>
  <h3>Instructions</h3>
  <ul>
  {% for key, instruction in template_instructions|dictsort %}
      <li>{{ instruction }}</li>
  {% endfor %}
  </ul>
  <h3>Comments</h3>
  <ul>
  {% for comment in template_comments %}
    <li>{{ comment }}</li>
  {% endfor %}
  </ul>
  <form method="POST">
  {{ template_form.hidden_tag() }}
  <!-- Insert StringField elements here -->


  <!-- Insert SubmitField element here -->

  </form>
{% endblock %}
