var LocalStorageManager = {
    setValue: function(key, value) {
        window.localStorage.setItem(key, JSON.stringify(value));
    },
    getValue: function(key) {
        try {
            return JSON.parse(window.localStorage.getItem(key));
        } catch (e) {

        }
    }
};

function myfunc() {
  let element = document.body;
  var alls = document.querySelectorAll("*");
  let btn = document.getElementById("mode");
  
  if (localStorage.getItem("tk") === "true"){
    btn.classList.add("sun");
  for (var i = 0; i < alls.length; i++) {
    alls[i].classList.add("t-dark");
  }
  }
  if (localStorage.getItem("tk") === "false"){
    btn.classList.remove("sun");
  for (var i = 0; i < alls.length; i++) {
    alls[i].classList.remove("t-dark");
  }
  }
  
};
 function check() {
   var input = document.getElementById("darker");
  input.addEventListener('click', function() {
    localStorage.setItem("tk", this.checked)
    myfunc();
  });
  console.log(localStorage.getItem("tk"))
 }
function double() {
  check();
  if (localStorage.getItem("tk") === "true"){
    myfunc();
  }
};


