<html>
  <head>
    <script type="text/javascript" src="/static/requests.js"> </script>
  </head>
  <body>
    <h1> TODO LIST </h1>
      {{ form.task.label }}{{form.task()}}
      <br>
      {{ form.date.label }}{{form.date(type='date')}}
      <br>
      {{form.butt(onclick="post_todo();get_todo();")}}

      <h2>Taks</h2>
      <div id="old_tasks">

      </div>
  </body>
</html>
