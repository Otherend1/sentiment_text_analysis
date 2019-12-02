const interval = setInterval(function() {
    var sentence = document.getElementById("textbox").value;
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_sentence', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    xhr.send("sentence=" + sentence);
    xhr.onreadystatechange = function (){
        var result = JSON.parse(this.response);
        var sentiment = Math.ceil(result["sentiment_intensity"]*100);
	update_bar(sentiment);
    }
},1000);

function update_bar(new_width) {
  var container1 = document.getElementById("bar1_container");
  var elem1 = document.getElementById("bar1");
  var width1 = document.getElementById("bar1").style.width;
  width1 = width1.replace("%", "");
	
  var container2 = document.getElementById("bar2_container");
  var elem2 = document.getElementById("bar2");
  var width2 = document.getElementById("bar2").style.width;
  width2 = width2.replace("%", "");
  
  var width = get_width(width1, width2);  
	
  var id = setInterval(frame, 5);
  function frame() {
    if (width == new_width) {
      clearInterval(id);
    }
    if (new_width>=50) {
      if (width2==100) {
        if (width1 < 2*(new_width - 50)) {
          width1++;
          elem1.style.width = width1 + '%';
        }
        if (width1 > 2*(new_width - 50)) {
          width1--;
          elem1.style.width = width1 + '%';
        }           
      } else {
          width2++;
          elem2.style.width = width2 + '%';
      }
  } else {
      if (width1==0) {
        if (100-width2 < 2*(50 - new_width)) {
          width2--;
          elem2.style.width = width2 + '%';
        }
        if (100-width2 > 2*(50 - new_width)) {
          width2++;
          elem2.style.width = width2 + '%';
        }
    } else {
        width1--;
        elem1.style.width = width1 + '%';
      }
    }
  }
}	

function get_width(width1, width2) {
  return(100-width1 + width2);
}


