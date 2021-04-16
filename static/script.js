function remove_alert(id){
    document.querySelector(id).style.display="none";
  }

function event_add(id){
  var btn = document.getElementById('removebtn').style.display;
  checkbox = document.getElementsByClassName("c"+ String(id))
  if(btn=="none" && checkbox[0].checked){
      document.getElementById('removebtn').style.display="block";
  }
  else{
      document.getElementById('removebtn').style.display="none";
  }
  
  document.getElementById('remove').addEventListener("click",function(){
      console.log("works")
      delete_task(id)
  })
}

function delete_task(id){
  var taskid="#task"+String(id)
  var formid="#form"+String(id)
  document.querySelector(taskid).className="text-decoration-line-through"
  document.querySelector(formid).submit()
}