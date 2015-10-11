#!/usr/bin/perl

#    WikiWork statistics calculator
#    Copyright (C) 2007-2008 Scott V. Nazelrod

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    See <http://www.gnu.org/licenses/> for a copy of the GPL.

$version = "0.4.1";
require "formparser.lib";

&parseform;

$fa = $formdata{'fa'};
$a  = $formdata{'a'};
$ga = $formdata{'ga'};
$b  = $formdata{'b'};
$c  = $formdata{'c'};
$start = $formdata{'start'};
$stub  = $formdata{'stub'};
$eds = $formdata{'eds'};
$subs = $formdata{'subs'};
$upper = $fa + $a + $ga;
$lower = $b + $c + $start + $stub;
$total = $fa + $a + $ga + $b + $c + $start + $stub;

#percentages
$fa_pct = $fa/$total * 100;
$a_pct = $a/$total * 100;
$ga_pct = $ga/$total * 100;
$b_pct = $b/$total * 100;
$c_pct = $c/$total * 100;
$start_pct = $start/$total * 100;
$stub_pct = $stub/$total * 100;
$upper_pct = $upper/$total * 100;
$lower_pct = $lower/$total * 100;

#rounded %s
$fa_pctrd= sprintf("%.2f", $fa_pct);
$a_pctrd= sprintf("%.2f", $a_pct);
$ga_pctrd= sprintf("%.2f", $ga_pct);
$b_pctrd= sprintf("%.2f", $b_pct);
$c_pctrd= sprintf("%.2f", $c_pct);
$start_pctrd= sprintf("%.2f", $start_pct);
$stub_pctrd= sprintf("%.2f", $stub_pct);
$upper_pctrd= sprintf("%.2f", $upper_pct);
$lower_pctrd= sprintf("%.2f", $lower_pct);

#wikiwork stats
$wikiwork = $a + 2*$ga + 3*$b + 4*$c + 5*$start + 6*$stub;
$rel = $wikiwork/$total;
$rel_rounded = sprintf("%.3f", $rel); #rounded to 3 dec places

#rel bar positioning
#$rel40 = $rel*40;
#$rel40_round = sprintf("%.0f", $rel40);
#$rel_pos =  $rel40_round."px";

#extra stats
if( $eds != 0 )
{
$ww_percapita = $wikiwork / $eds;
$capitastring = "<li><b>&omega; per capita</b> = $ww_percapita</li>";
}

if( $subs != 0)
{
$ww_subprojs = $wikiwork / $subs;
$subprojstring = "<li><b>&omega; per capita</b> = $ww_subprojs</li>";
}

print << "DOC";
Content-type:text/html\n\n
<!--Output by WikiWork Calculator v.$version by Scott Nazelrod-->

<html>
<head>
<link rel="stylesheet" href="http://www.scott5114.name/style.css" type="text/css" />
<title>WikiWork calculator</title>
<style type="text/css">
body{ background-image: url(http://www.scott5114.name/headbg.jpg); background-repeat:no-repeat; }

table.wikitable,
table.prettytable {
  margin: 1em 1em 1em 0;
  background: #f9f9f9;
  border: 1px #aaa solid;
  border-collapse: collapse;
}
 
table.wikitable th, table.wikitable td,
table.prettytable th, table.prettytable td {
  border: 1px #aaa solid;
  padding: 0.2em;
}
 
table.wikitable th,
table.prettytable th {
  background: #f2f2f2;
  text-align: center;
}
 
table.wikitable caption,
table.prettytable caption {
  margin-left: inherit;
  margin-right: inherit;
  font-weight: bold;
}

table.wikitable code {
  background-color: transparent;
}

.relbar {
position:relative;
width:200px; 
height:20px;
}

#pointer {
position:absolute; 
top:-5px; 
left:$rel_pos;
}
</style>
</head>

<body>
<h1 id="title">Results</h1>

<table class="wikitable" style="text-align: center; float:left">

<tr>
	<th style="text-align: center;">Article class</th>
	<th style="text-align: center;">Articles</th>
	<th style="text-align: center;">Percent</th>
</tr>

<tr><th style="background: #6699ff; text-align: center;"><img alt="Featured article" src="fa.png"/>&nbsp;FA</th>
<td>$fa</td>
<td>$fa_pctrd %<!--$fa_pct --></td>
</tr>

<tr>
<th style="background: #66ffff; text-align: center;">A</th>
<td>$a</td>
<td>$a_pctrd %<!--$a_pct --></td>
</tr>

<tr>
<th style="background: #66ff66; text-align: center;"><img alt="Good article" src="ga.png"/>&nbsp;GA</th>
<td>$ga</td>
<td>$ga_pctrd %<!--$ga_pct --></td>
</tr>

<tr>
<th style="background: #c8fb7b; text-align: center;">B</th>
<td>$b</td>
<td>$b_pctrd %<!--$b_pct --></td>
</tr>

<tr>
<th style="background: #ffff66; text-align: center;">C</th>
<td>$c</td>
<td>$c_pctrd %<!--$c_pct --></td>
</tr>

<tr>
<th style="background: #ffaa66; text-align: center;">Start</th>
<td>$start</td>
<td>$start_pctrd %<!--$start_pct --></td>
</tr>

<tr>
<th style="background: #ff6666; text-align: center;">Stub</th>
<td>$stub</td>
<td>$stub_pctrd %<!--$stub_pct --></td>
</tr>

<tr>
<th style="background: transparent; text-align: center">Total</th>
<td>$total</td>
<td/>
</tr>
</table>

<h2>WikiWork statistics</h2>
<ul>
<li><b>&omega;</b> = $wikiwork</li>
<li><b>&Omega;</b> = $rel_rounded <!--$rel --></li>
$capitastring
$subprojstring
<li><b>Upper half:</b> (articles that are FA, A, and GA classes): $upper_pctrd%
<li><b>Lower half:</b> (articles that are B, C, Start, Stub classes): $lower_pctrd%
</ul>

<!--<br class="clear"/>-->

<!--<h2>Graphical analysis</h2>-->
<!--<h2>&Omega;</h2>-->

<!--<div class="relbar"><img src="wgradient.png" alt="&Omega;"/><img src="wpointer.png" alt="$rel_rounded" id="pointer"/></div>-->

<p><a href="wikiwork.html" id="relpointer">Return to input page</a> - <a href="index.html">Back to Programs</a></p>

</body>
</html>

DOC

