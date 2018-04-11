<html>
  <head>
    <script type="text/javascript" src="/static/requests.js"> </script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <body>
  <div class="form-group col-sm-3 mx-auto">
      <h1> TODO LIST </h1>

      {{ form.task.label }}{{form.task(class_="form-control")}}
      <br>
      {{ form.date.label }}{{form.date(class_="form-control", type='date')}}
      <br>
      {{form.butt(class_="btn btn-outline-dark form-control", onclick="post_todo();get_todo();")}}
      {{form.butt_s(class_="btn btn-outline-dark form-control", onclick="get_todo();")}}
      <h2>Taks</h2>
  </div>

      <table id="old_tasks" class="table table-striped table-dark">

      </table>
  </body>
</html>
