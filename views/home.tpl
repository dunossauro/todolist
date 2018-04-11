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
      {{form.butt(onclick="post_todo();")}}
      {{form.butt_s(onclick="get_todo();")}}

      <h2>Taks</h2>
      <table id="old_tasks">

      </table>
  </body>
</html>
