<!DOCTYPE html>
<html>
  <body>
    <a href="/">Back To Recipe List</a>
    <h1>{{ template_recipe | title }}</h1>
    <!-- Insert description if statement here -->

    {% if template_description %}
        <p>{{ template_description }}</p>
    {% else %}
    <!-- Include else here -->
        <p>A {{ template_description }} recipe.</p>
    {% endif %}

    <p>A {{ template_recipe }} recipe.</p>
    <!-- Be sure to close with an endif block -->

    <h3>Ingredients - {{ template_ingredients | length}}</h3>
    <ul>
      <li>{{ template_ingredients[0] }}</li>
      <li>{{ template_ingredients[1] }}</li>
      <!-- Insert ingredient if statement -->

      {% if  template_ingredients | length == 3%}

      <li>{{ template_ingredients[2] }}</li>
      <!-- Be sure to close with an endif block -->

      {% endif %}

    </ul>
    <h3>Instructions</h3>
    <ol>
      <li>{{ template_instructions | dictsort }}</li>
    </ol>
  </body>
</html>
