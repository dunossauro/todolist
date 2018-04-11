function write_table(task_json){
     var table = document.getElementById('old_tasks')
     table.innerHTML = task_json.map(task =>
          `<tr><td>${task.task}</td>
           <td>${task.date}</td></tr>`
      ).join('')
  }

function get_todo(){
   fetch('http://127.0.0.1:8080/get_tasks')
    .then(response => response.json())
    .then(myJSON => write_table(myJSON))
}


function post_todo() {
  return fetch('http://127.0.0.1:8080/post_tasks', {
    body: JSON.stringify({task: document.getElementById("task").value,
                          date: document.getElementById("date").value}),
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'content-type': 'application/json'
    },
    method: 'POST',
    mode: 'cors',
    redirect: 'follow',
    referrer: 'no-referrer',
  })
  .then(response => response.json())
}

get_todo()
