<html>
  <head>
    <script type="text/javascript" src="/static/oi.js"> </script>
  </head>
  <body>
    <h1> TODO LIST </h1>
      {{ form.task.label }}{{form.task()}}
      <br>
      {{ form.date.label }}{{form.date(type='date')}}
      <br>
      {{form.butt(onclick="post_todo();")}}
  </body>
</html>
