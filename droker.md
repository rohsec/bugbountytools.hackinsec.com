---
title: 🚀 Google Dorker
layout: default
nav_order: 2
---

# **🚀 Google Dorker** 
---
<link rel="stylesheet" href="styles.css" />
<link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
<script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
Domain
<input type="text" class="cus_inp1" id="inp" placeholder="Enter a domain...">
<div id="warn" class="warn"></div>
<button type="button" name="button" class="btn btn-blue" py-click="dorker">Update Domain</button>

<script type="py" src="dork.py" config="config.json" target="out"></script>
<div id="out">    
        <!-- <h1>This is box</h1> -->
</div>