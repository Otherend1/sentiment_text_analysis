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
  var elem = document.getElementById("bar");
  var width = document.getElementById("bar").style.width;
  width = width.replace("%", "");
  var id = setInterval(frame, 20);
  function frame() {
    if (width == new_width) {
      clearInterval(id);
    }
    if (width < new_width) {
      width++;
      elem.style.width = width + '%';
      elem.innerHTML = width * 1  + '%';
    }
    if (width > new_width) {
      width--;
      elem.style.width = width + '%';
      elem.innerHTML = width * 1  + '%';
    }
  }
}
