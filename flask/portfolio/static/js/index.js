import { Remarkable } from 'remarkable';
var md = new Remarkable();
fetch("https://raw.githubusercontent.com/viperML/flaskapp/main/README.md")
.then((response) => response.text())
.then((html) => {
    document.getElementById("DATA").innerHTML = md.render(html);
})