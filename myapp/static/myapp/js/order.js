var room = 1;
function add_input_fields() {
 
    room++;
    var objTo = document.getElementById('add_input_fields')
    var tr = document.createElement("tr");
	// divtest.setAttribute("class", "form-group removeclass"+room);
	// var rdiv = 'removeclass'+room;
    tr.innerHTML = '<tr><td><input type="text" class="form-control" placeholder="Item" /></td><td><input type="text" class="form-control" placeholder="Quantity" /></td><td><input type="text" class="form-control" placeholder="Rate" id="total" /></td></tr>';
    
    objTo.appendChild(tr)
}

function handleEnter(e){
    var keycode = (e.keyCode ? e.keyCode : e.which);
    if (keycode == '13') {
      // alert('You pressed enter! - plain javascript');
      add_input_fields();
    }
}

function generate_total(){
    
}

