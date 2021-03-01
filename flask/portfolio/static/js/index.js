import {Remarkable}  from 'remarkable';
// Material Design Bootstrap dependencies
import $ from "jquery";
import '@popperjs/core';
import 'bootstrap';
import * as mdb from 'mdb-ui-kit';


var md = new Remarkable();

fetch("https://raw.githubusercontent.com/viperML/flaskapp/main/README.md")
.then((response) => response.text())
.then((html) => {
    document.getElementById("README").innerHTML = md.render(html);
})

