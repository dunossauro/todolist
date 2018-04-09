function get_todo(){
   fetch('http://127.0.0.1:8080/fetch')
    .then(response => response.json())
    .then(myJson => console.log(myJson));
}


function post_todo() {
  return fetch('http://127.0.0.1:8080/fetchp', {
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
