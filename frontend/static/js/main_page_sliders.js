var slider = document.getElementById("myRange");
var output = document.getElementById("maxTweets");
output.innerHTML = slider.value;
slider.oninput = function() {
  output.innerHTML = this.value;
  if(this.value === "100000") {
    output.innerHTML = "100000+";
  }
}