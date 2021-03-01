import { Remarkable } from 'remarkable';
import * as mdb from 'mdb-ui-kit'; // lib
import $ from "jquery";
import '@popperjs/core';
import 'bootstrap';

var md = new Remarkable();

fetch("https://raw.githubusercontent.com/viperML/flaskapp/main/README.md")
.then((response) => response.text())
.then((html) => {
    document.getElementById("DATA").innerHTML = md.render(html);
})