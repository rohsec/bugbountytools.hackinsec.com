---
title: 🔄 Replacer
layout: default
nav_order: 3
---

## 🔄 Replacer
---
Enter URLs(one per line):
<link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
<script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
<link rel="stylesheet" href="styles.css" />
<textarea class="cus_txt" id="txt1"></textarea>
Source

<input type="text" class="cus_inp" id="rep" placeholder="Word to Replace...">

Target

<input type="text" class="cus_inp" id="rep1" placeholder="Word to be Replaced...">

<button type="button" name="button" class="btn btn-blue" mpy-click="replacer">Replace</button>
<div id="warn" class="warn"></div>
<script type="mpy" src="replace.py"></script>
<div id="out">    
        <!-- <h1>This is box</h1> -->
</div>