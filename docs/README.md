<link rel='stylesheet' href="assets/style.css">
<link rel='stylesheet' href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin="">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script type="text/javascript"  src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"></script>
<script type="text/javascript" src="assets/actions.js"></script>

![Build Status](https://github.com/CBIIT/cda-model/actions/workflows/model-test-and-deploy.yml/badge.svg)

# Cancer Data Aggregator Data Model

[CDA data model](https://github.com/CancerDataAggregator/cda-data-model) in MDF format.

[View model on GitHub Pages](https://cbiit.github.io/cda-model)


Zoom to Node: <select id="node_select">
  <option value="">Zoom to Node</option>
</select>
<div id="model"></div>

<p>
<a href="./model-desc/cda-model.svg">SVG file (in view above)</a>
<p>
<a href="./model-desc">Additional model files</a>
<div id='graph' style='display:off;'>
<svg width="1872pt" height="1396pt"
 viewBox="0.00 0.00 1872.00 1396.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 1392)">
<title>Perl</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-1392 1868,-1392 1868,4 -4,4"/>
<!-- Specimen -->
<g id="node1" class="node">
<title>Specimen</title>
<path fill="none" stroke="#000000" d="M48,-1088.5C48,-1088.5 368,-1088.5 368,-1088.5 374,-1088.5 380,-1094.5 380,-1100.5 380,-1100.5 380,-1375.5 380,-1375.5 380,-1381.5 374,-1387.5 368,-1387.5 368,-1387.5 48,-1387.5 48,-1387.5 42,-1387.5 36,-1381.5 36,-1375.5 36,-1375.5 36,-1100.5 36,-1100.5 36,-1094.5 42,-1088.5 48,-1088.5"/>
<text text-anchor="middle" x="79.5" y="-1234.3" font-family="Times,serif" font-size="14.00" fill="#000000">Specimen</text>
<polyline fill="none" stroke="#000000" points="123,-1088.5 123,-1387.5 "/>
<text text-anchor="middle" x="133.5" y="-1234.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="144,-1088.5 144,-1387.5 "/>
<text text-anchor="middle" x="251.5" y="-1372.3" font-family="Times,serif" font-size="14.00" fill="#000000">age_at_collection</text>
<polyline fill="none" stroke="#000000" points="144,-1364.5 359,-1364.5 "/>
<text text-anchor="middle" x="251.5" y="-1349.3" font-family="Times,serif" font-size="14.00" fill="#000000">analyte_type</text>
<polyline fill="none" stroke="#000000" points="144,-1341.5 359,-1341.5 "/>
<text text-anchor="middle" x="251.5" y="-1326.3" font-family="Times,serif" font-size="14.00" fill="#000000">anatomical_site</text>
<polyline fill="none" stroke="#000000" points="144,-1318.5 359,-1318.5 "/>
<text text-anchor="middle" x="251.5" y="-1303.3" font-family="Times,serif" font-size="14.00" fill="#000000">cellular_composition</text>
<polyline fill="none" stroke="#000000" points="144,-1295.5 359,-1295.5 "/>
<text text-anchor="middle" x="251.5" y="-1280.3" font-family="Times,serif" font-size="14.00" fill="#000000">derived_from_specimen</text>
<polyline fill="none" stroke="#000000" points="144,-1272.5 359,-1272.5 "/>
<text text-anchor="middle" x="251.5" y="-1257.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="144,-1249.5 359,-1249.5 "/>
<text text-anchor="middle" x="251.5" y="-1234.3" font-family="Times,serif" font-size="14.00" fill="#000000">general_tissue_morphology</text>
<polyline fill="none" stroke="#000000" points="144,-1226.5 359,-1226.5 "/>
<text text-anchor="middle" x="251.5" y="-1211.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="144,-1203.5 359,-1203.5 "/>
<text text-anchor="middle" x="251.5" y="-1188.3" font-family="Times,serif" font-size="14.00" fill="#000000">matched_normal_flag</text>
<polyline fill="none" stroke="#000000" points="144,-1180.5 359,-1180.5 "/>
<text text-anchor="middle" x="251.5" y="-1165.3" font-family="Times,serif" font-size="14.00" fill="#000000">qualification_status_flag</text>
<polyline fill="none" stroke="#000000" points="144,-1157.5 359,-1157.5 "/>
<text text-anchor="middle" x="251.5" y="-1142.3" font-family="Times,serif" font-size="14.00" fill="#000000">source_material_type</text>
<polyline fill="none" stroke="#000000" points="144,-1134.5 359,-1134.5 "/>
<text text-anchor="middle" x="251.5" y="-1119.3" font-family="Times,serif" font-size="14.00" fill="#000000">specific_tissue_morphology</text>
<polyline fill="none" stroke="#000000" points="144,-1111.5 359,-1111.5 "/>
<text text-anchor="middle" x="251.5" y="-1096.3" font-family="Times,serif" font-size="14.00" fill="#000000">specimen_type</text>
<polyline fill="none" stroke="#000000" points="359,-1088.5 359,-1387.5 "/>
<text text-anchor="middle" x="369.5" y="-1234.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Identifier -->
<g id="node2" class="node">
<title>Identifier</title>
<path fill="none" stroke="#000000" d="M418,-23.5C418,-23.5 648,-23.5 648,-23.5 654,-23.5 660,-29.5 660,-35.5 660,-35.5 660,-80.5 660,-80.5 660,-86.5 654,-92.5 648,-92.5 648,-92.5 418,-92.5 418,-92.5 412,-92.5 406,-86.5 406,-80.5 406,-80.5 406,-35.5 406,-35.5 406,-29.5 412,-23.5 418,-23.5"/>
<text text-anchor="middle" x="448" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">Identifier</text>
<polyline fill="none" stroke="#000000" points="490,-23.5 490,-92.5 "/>
<text text-anchor="middle" x="500.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="511,-23.5 511,-92.5 "/>
<text text-anchor="middle" x="575" y="-77.3" font-family="Times,serif" font-size="14.00" fill="#000000">identifier_value</text>
<polyline fill="none" stroke="#000000" points="511,-69.5 639,-69.5 "/>
<text text-anchor="middle" x="575" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="511,-46.5 639,-46.5 "/>
<text text-anchor="middle" x="575" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">type</text>
<polyline fill="none" stroke="#000000" points="639,-23.5 639,-92.5 "/>
<text text-anchor="middle" x="649.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Specimen&#45;&gt;Identifier -->
<g id="edge10" class="edge">
<title>Specimen&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M51.683,-1088.4536C21.9964,-1045.7076 0,-996.4923 0,-944.5 0,-944.5 0,-944.5 0,-259.5 0,-208.4754 25.7874,-195.6637 68,-167 120.8656,-131.1026 278.6356,-98.9188 395.8243,-78.9897"/>
<polygon fill="#000000" stroke="#000000" points="396.6857,-82.3939 405.9639,-77.2786 395.5209,-75.4915 396.6857,-82.3939"/>
<text text-anchor="middle" x="33.5" y="-655.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Patient -->
<g id="node5" class="node">
<title>Patient</title>
<path fill="none" stroke="#000000" d="M108,-852.5C108,-852.5 308,-852.5 308,-852.5 314,-852.5 320,-858.5 320,-864.5 320,-864.5 320,-1024.5 320,-1024.5 320,-1030.5 314,-1036.5 308,-1036.5 308,-1036.5 108,-1036.5 108,-1036.5 102,-1036.5 96,-1030.5 96,-1024.5 96,-1024.5 96,-864.5 96,-864.5 96,-858.5 102,-852.5 108,-852.5"/>
<text text-anchor="middle" x="130" y="-940.8" font-family="Times,serif" font-size="14.00" fill="#000000">Patient</text>
<polyline fill="none" stroke="#000000" points="164,-852.5 164,-1036.5 "/>
<text text-anchor="middle" x="174.5" y="-940.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="185,-852.5 185,-1036.5 "/>
<text text-anchor="middle" x="242" y="-1021.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_to_birth</text>
<polyline fill="none" stroke="#000000" points="185,-1013.5 299,-1013.5 "/>
<text text-anchor="middle" x="242" y="-998.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="185,-990.5 299,-990.5 "/>
<text text-anchor="middle" x="242" y="-975.3" font-family="Times,serif" font-size="14.00" fill="#000000">ethnicity</text>
<polyline fill="none" stroke="#000000" points="185,-967.5 299,-967.5 "/>
<text text-anchor="middle" x="242" y="-952.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="185,-944.5 299,-944.5 "/>
<text text-anchor="middle" x="242" y="-929.3" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="185,-921.5 299,-921.5 "/>
<text text-anchor="middle" x="242" y="-906.3" font-family="Times,serif" font-size="14.00" fill="#000000">race</text>
<polyline fill="none" stroke="#000000" points="185,-898.5 299,-898.5 "/>
<text text-anchor="middle" x="242" y="-883.3" font-family="Times,serif" font-size="14.00" fill="#000000">sex</text>
<polyline fill="none" stroke="#000000" points="185,-875.5 299,-875.5 "/>
<text text-anchor="middle" x="242" y="-860.3" font-family="Times,serif" font-size="14.00" fill="#000000">taxon</text>
<polyline fill="none" stroke="#000000" points="299,-852.5 299,-1036.5 "/>
<text text-anchor="middle" x="309.5" y="-940.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Specimen&#45;&gt;Patient -->
<g id="edge6" class="edge">
<title>Specimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M208,-1088.2407C208,-1074.276 208,-1060.3477 208,-1046.9618"/>
<polygon fill="#000000" stroke="#000000" points="211.5001,-1046.8397 208,-1036.8397 204.5001,-1046.8398 211.5001,-1046.8397"/>
<text text-anchor="middle" x="286" y="-1058.8" font-family="Times,serif" font-size="14.00" fill="#000000">derived_from_subject</text>
</g>
<!-- Study -->
<g id="node3" class="node">
<title>Study</title>
<path fill="none" stroke="#000000" d="M853.5,-.5C853.5,-.5 1068.5,-.5 1068.5,-.5 1074.5,-.5 1080.5,-6.5 1080.5,-12.5 1080.5,-12.5 1080.5,-103.5 1080.5,-103.5 1080.5,-109.5 1074.5,-115.5 1068.5,-115.5 1068.5,-115.5 853.5,-115.5 853.5,-115.5 847.5,-115.5 841.5,-109.5 841.5,-103.5 841.5,-103.5 841.5,-12.5 841.5,-12.5 841.5,-6.5 847.5,-.5 853.5,-.5"/>
<text text-anchor="middle" x="871" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">Study</text>
<polyline fill="none" stroke="#000000" points="900.5,-.5 900.5,-115.5 "/>
<text text-anchor="middle" x="911" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="921.5,-.5 921.5,-115.5 "/>
<text text-anchor="middle" x="990.5" y="-100.3" font-family="Times,serif" font-size="14.00" fill="#000000">dbgap_accession</text>
<polyline fill="none" stroke="#000000" points="921.5,-92.5 1059.5,-92.5 "/>
<text text-anchor="middle" x="990.5" y="-77.3" font-family="Times,serif" font-size="14.00" fill="#000000">embargo_date</text>
<polyline fill="none" stroke="#000000" points="921.5,-69.5 1059.5,-69.5 "/>
<text text-anchor="middle" x="990.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">identifier_value</text>
<polyline fill="none" stroke="#000000" points="921.5,-46.5 1059.5,-46.5 "/>
<text text-anchor="middle" x="990.5" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">study_label</text>
<polyline fill="none" stroke="#000000" points="921.5,-23.5 1059.5,-23.5 "/>
<text text-anchor="middle" x="990.5" y="-8.3" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="1059.5,-.5 1059.5,-115.5 "/>
<text text-anchor="middle" x="1070" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- File -->
<g id="node4" class="node">
<title>File</title>
<path fill="none" stroke="#000000" d="M565,-403.5C565,-403.5 787,-403.5 787,-403.5 793,-403.5 799,-409.5 799,-415.5 799,-415.5 799,-621.5 799,-621.5 799,-627.5 793,-633.5 787,-633.5 787,-633.5 565,-633.5 565,-633.5 559,-633.5 553,-627.5 553,-621.5 553,-621.5 553,-415.5 553,-415.5 553,-409.5 559,-403.5 565,-403.5"/>
<text text-anchor="middle" x="575" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">File</text>
<polyline fill="none" stroke="#000000" points="597,-403.5 597,-633.5 "/>
<text text-anchor="middle" x="607.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="618,-403.5 618,-633.5 "/>
<text text-anchor="middle" x="698" y="-618.3" font-family="Times,serif" font-size="14.00" fill="#000000">byte_size</text>
<polyline fill="none" stroke="#000000" points="618,-610.5 778,-610.5 "/>
<text text-anchor="middle" x="698" y="-595.3" font-family="Times,serif" font-size="14.00" fill="#000000">checksum</text>
<polyline fill="none" stroke="#000000" points="618,-587.5 778,-587.5 "/>
<text text-anchor="middle" x="698" y="-572.3" font-family="Times,serif" font-size="14.00" fill="#000000">data_category</text>
<polyline fill="none" stroke="#000000" points="618,-564.5 778,-564.5 "/>
<text text-anchor="middle" x="698" y="-549.3" font-family="Times,serif" font-size="14.00" fill="#000000">data_type</text>
<polyline fill="none" stroke="#000000" points="618,-541.5 778,-541.5 "/>
<text text-anchor="middle" x="698" y="-526.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="618,-518.5 778,-518.5 "/>
<text text-anchor="middle" x="698" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">file_format</text>
<polyline fill="none" stroke="#000000" points="618,-495.5 778,-495.5 "/>
<text text-anchor="middle" x="698" y="-480.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="618,-472.5 778,-472.5 "/>
<text text-anchor="middle" x="698" y="-457.3" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="618,-449.5 778,-449.5 "/>
<text text-anchor="middle" x="698" y="-434.3" font-family="Times,serif" font-size="14.00" fill="#000000">media_type</text>
<polyline fill="none" stroke="#000000" points="618,-426.5 778,-426.5 "/>
<text text-anchor="middle" x="698" y="-411.3" font-family="Times,serif" font-size="14.00" fill="#000000">reference_assembly</text>
<polyline fill="none" stroke="#000000" points="778,-403.5 778,-633.5 "/>
<text text-anchor="middle" x="788.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- File&#45;&gt;Identifier -->
<g id="edge11" class="edge">
<title>File&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M657.1886,-403.3151C642.3363,-317.8473 621.3048,-209.1355 604,-167 594.5083,-143.8886 579.961,-120.3965 566.5002,-101.1688"/>
<polygon fill="#000000" stroke="#000000" points="569.2752,-99.0321 560.6156,-92.9279 563.5785,-103.1001 569.2752,-99.0321"/>
<text text-anchor="middle" x="681.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Project -->
<g id="node6" class="node">
<title>Project</title>
<path fill="none" stroke="#000000" d="M849,-167.5C849,-167.5 1073,-167.5 1073,-167.5 1079,-167.5 1085,-173.5 1085,-179.5 1085,-179.5 1085,-339.5 1085,-339.5 1085,-345.5 1079,-351.5 1073,-351.5 1073,-351.5 849,-351.5 849,-351.5 843,-351.5 837,-345.5 837,-339.5 837,-339.5 837,-179.5 837,-179.5 837,-173.5 843,-167.5 849,-167.5"/>
<text text-anchor="middle" x="871" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">Project</text>
<polyline fill="none" stroke="#000000" points="905,-167.5 905,-351.5 "/>
<text text-anchor="middle" x="915.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="926,-167.5 926,-351.5 "/>
<text text-anchor="middle" x="995" y="-336.3" font-family="Times,serif" font-size="14.00" fill="#000000">dbgap_accession</text>
<polyline fill="none" stroke="#000000" points="926,-328.5 1064,-328.5 "/>
<text text-anchor="middle" x="995" y="-313.3" font-family="Times,serif" font-size="14.00" fill="#000000">dct_title</text>
<polyline fill="none" stroke="#000000" points="926,-305.5 1064,-305.5 "/>
<text text-anchor="middle" x="995" y="-290.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="926,-282.5 1064,-282.5 "/>
<text text-anchor="middle" x="995" y="-267.3" font-family="Times,serif" font-size="14.00" fill="#000000">disease_site</text>
<polyline fill="none" stroke="#000000" points="926,-259.5 1064,-259.5 "/>
<text text-anchor="middle" x="995" y="-244.3" font-family="Times,serif" font-size="14.00" fill="#000000">disease_type</text>
<polyline fill="none" stroke="#000000" points="926,-236.5 1064,-236.5 "/>
<text text-anchor="middle" x="995" y="-221.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="926,-213.5 1064,-213.5 "/>
<text text-anchor="middle" x="995" y="-198.3" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="926,-190.5 1064,-190.5 "/>
<text text-anchor="middle" x="995" y="-175.3" font-family="Times,serif" font-size="14.00" fill="#000000">program</text>
<polyline fill="none" stroke="#000000" points="1064,-167.5 1064,-351.5 "/>
<text text-anchor="middle" x="1074.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- File&#45;&gt;Project -->
<g id="edge17" class="edge">
<title>File&#45;&gt;Project</title>
<path fill="none" stroke="#000000" d="M656.7617,-403.1376C658.9572,-391.3039 663.1131,-379.9818 670,-370 672.566,-366.2809 751.9167,-336.2733 827.1004,-308.4681"/>
<polygon fill="#000000" stroke="#000000" points="828.5508,-311.6636 836.718,-304.9148 826.1248,-305.0974 828.5508,-311.6636"/>
<text text-anchor="middle" x="737.5" y="-373.8" font-family="Times,serif" font-size="14.00" fill="#000000">associated_project</text>
</g>
<!-- Patient&#45;&gt;Identifier -->
<g id="edge9" class="edge">
<title>Patient&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M121.3489,-852.4135C99.443,-820.2491 82,-782.2991 82,-743 82,-743 82,-743 82,-259.5 82,-205.436 115.615,-196.3789 161,-167 231.5582,-121.3259 321.8104,-94.2741 395.7473,-78.5452"/>
<polygon fill="#000000" stroke="#000000" points="396.5268,-81.9581 405.6042,-76.4945 395.1009,-75.1048 396.5268,-81.9581"/>
<text text-anchor="middle" x="115.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- ResearchSubject -->
<g id="node13" class="node">
<title>ResearchSubject</title>
<path fill="none" stroke="#000000" d="M387,-685.5C387,-685.5 743,-685.5 743,-685.5 749,-685.5 755,-691.5 755,-697.5 755,-697.5 755,-788.5 755,-788.5 755,-794.5 749,-800.5 743,-800.5 743,-800.5 387,-800.5 387,-800.5 381,-800.5 375,-794.5 375,-788.5 375,-788.5 375,-697.5 375,-697.5 375,-691.5 381,-685.5 387,-685.5"/>
<text text-anchor="middle" x="444" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000">ResearchSubject</text>
<polyline fill="none" stroke="#000000" points="513,-685.5 513,-800.5 "/>
<text text-anchor="middle" x="523.5" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="534,-685.5 534,-800.5 "/>
<text text-anchor="middle" x="634" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="534,-777.5 734,-777.5 "/>
<text text-anchor="middle" x="634" y="-762.3" font-family="Times,serif" font-size="14.00" fill="#000000">harmonized_disease_type</text>
<polyline fill="none" stroke="#000000" points="534,-754.5 734,-754.5 "/>
<text text-anchor="middle" x="634" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="534,-731.5 734,-731.5 "/>
<text text-anchor="middle" x="634" y="-716.3" font-family="Times,serif" font-size="14.00" fill="#000000">primary_disease_site</text>
<polyline fill="none" stroke="#000000" points="534,-708.5 734,-708.5 "/>
<text text-anchor="middle" x="634" y="-693.3" font-family="Times,serif" font-size="14.00" fill="#000000">primary_disease_type</text>
<polyline fill="none" stroke="#000000" points="734,-685.5 734,-800.5 "/>
<text text-anchor="middle" x="744.5" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Patient&#45;&gt;ResearchSubject -->
<g id="edge22" class="edge">
<title>Patient&#45;&gt;ResearchSubject</title>
<path fill="none" stroke="#000000" d="M300.8413,-852.3767C315.8806,-840.1426 331.8427,-828.5508 348,-819 356.3759,-814.0489 365.1241,-809.3516 374.0978,-804.9047"/>
<polygon fill="#000000" stroke="#000000" points="375.6558,-808.0391 383.1411,-800.5411 372.6137,-801.7347 375.6558,-808.0391"/>
<text text-anchor="middle" x="425" y="-822.8" font-family="Times,serif" font-size="14.00" fill="#000000">research_subject_list</text>
</g>
<!-- Project&#45;&gt;Study -->
<g id="edge4" class="edge">
<title>Project&#45;&gt;Study</title>
<path fill="none" stroke="#000000" d="M961,-167.3007C961,-153.2623 961,-139.0009 961,-125.6174"/>
<polygon fill="#000000" stroke="#000000" points="964.5001,-125.5721 961,-115.5722 957.5001,-125.5722 964.5001,-125.5721"/>
<text text-anchor="middle" x="987" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">studies</text>
</g>
<!-- Coding -->
<g id="node14" class="node">
<title>Coding</title>
<path fill="none" stroke="#000000" d="M1192.5,-12C1192.5,-12 1347.5,-12 1347.5,-12 1353.5,-12 1359.5,-18 1359.5,-24 1359.5,-24 1359.5,-92 1359.5,-92 1359.5,-98 1353.5,-104 1347.5,-104 1347.5,-104 1192.5,-104 1192.5,-104 1186.5,-104 1180.5,-98 1180.5,-92 1180.5,-92 1180.5,-24 1180.5,-24 1180.5,-18 1186.5,-12 1192.5,-12"/>
<text text-anchor="middle" x="1214.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">Coding</text>
<polyline fill="none" stroke="#000000" points="1248.5,-12 1248.5,-104 "/>
<text text-anchor="middle" x="1259" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1269.5,-12 1269.5,-104 "/>
<text text-anchor="middle" x="1304" y="-88.8" font-family="Times,serif" font-size="14.00" fill="#000000">code</text>
<polyline fill="none" stroke="#000000" points="1269.5,-81 1338.5,-81 "/>
<text text-anchor="middle" x="1304" y="-65.8" font-family="Times,serif" font-size="14.00" fill="#000000">display</text>
<polyline fill="none" stroke="#000000" points="1269.5,-58 1338.5,-58 "/>
<text text-anchor="middle" x="1304" y="-42.8" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="1269.5,-35 1338.5,-35 "/>
<text text-anchor="middle" x="1304" y="-19.8" font-family="Times,serif" font-size="14.00" fill="#000000">version</text>
<polyline fill="none" stroke="#000000" points="1338.5,-12 1338.5,-104 "/>
<text text-anchor="middle" x="1349" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Project&#45;&gt;Coding -->
<g id="edge8" class="edge">
<title>Project&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1085.1037,-172.8782C1088.0926,-170.8919 1091.0614,-168.9299 1094,-167 1123.267,-147.7792 1155.7473,-127.402 1184.7566,-109.5321"/>
<polygon fill="#000000" stroke="#000000" points="1186.9545,-112.2894 1193.6407,-104.0708 1183.2887,-106.3261 1186.9545,-112.2894"/>
<text text-anchor="middle" x="1175.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Treatment -->
<g id="node7" class="node">
<title>Treatment</title>
<path fill="none" stroke="#000000" d="M182.5,-190.5C182.5,-190.5 485.5,-190.5 485.5,-190.5 491.5,-190.5 497.5,-196.5 497.5,-202.5 497.5,-202.5 497.5,-316.5 497.5,-316.5 497.5,-322.5 491.5,-328.5 485.5,-328.5 485.5,-328.5 182.5,-328.5 182.5,-328.5 176.5,-328.5 170.5,-322.5 170.5,-316.5 170.5,-316.5 170.5,-202.5 170.5,-202.5 170.5,-196.5 176.5,-190.5 182.5,-190.5"/>
<text text-anchor="middle" x="216.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">Treatment</text>
<polyline fill="none" stroke="#000000" points="262.5,-190.5 262.5,-328.5 "/>
<text text-anchor="middle" x="273" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="283.5,-190.5 283.5,-328.5 "/>
<text text-anchor="middle" x="380" y="-313.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_to_treatment_start</text>
<polyline fill="none" stroke="#000000" points="283.5,-305.5 476.5,-305.5 "/>
<text text-anchor="middle" x="380" y="-290.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_treatment_end</text>
<polyline fill="none" stroke="#000000" points="283.5,-282.5 476.5,-282.5 "/>
<text text-anchor="middle" x="380" y="-267.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="283.5,-259.5 476.5,-259.5 "/>
<text text-anchor="middle" x="380" y="-244.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="283.5,-236.5 476.5,-236.5 "/>
<text text-anchor="middle" x="380" y="-221.3" font-family="Times,serif" font-size="14.00" fill="#000000">treatment_outcome</text>
<polyline fill="none" stroke="#000000" points="283.5,-213.5 476.5,-213.5 "/>
<text text-anchor="middle" x="380" y="-198.3" font-family="Times,serif" font-size="14.00" fill="#000000">treatment_type</text>
<polyline fill="none" stroke="#000000" points="476.5,-190.5 476.5,-328.5 "/>
<text text-anchor="middle" x="487" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Treatment&#45;&gt;Identifier -->
<g id="edge12" class="edge">
<title>Treatment&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M397.539,-190.3673C414.965,-171.8368 434.0155,-151.9657 452,-134 463.303,-122.7088 475.774,-110.7657 487.473,-99.7754"/>
<polygon fill="#000000" stroke="#000000" points="490.1172,-102.0945 495.0294,-92.7072 485.3354,-96.9824 490.1172,-102.0945"/>
<text text-anchor="middle" x="485.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Quantity -->
<g id="node8" class="node">
<title>Quantity</title>
<path fill="none" stroke="#000000" d="M1363.5,-241.5C1363.5,-241.5 1516.5,-241.5 1516.5,-241.5 1522.5,-241.5 1528.5,-247.5 1528.5,-253.5 1528.5,-253.5 1528.5,-265.5 1528.5,-265.5 1528.5,-271.5 1522.5,-277.5 1516.5,-277.5 1516.5,-277.5 1363.5,-277.5 1363.5,-277.5 1357.5,-277.5 1351.5,-271.5 1351.5,-265.5 1351.5,-265.5 1351.5,-253.5 1351.5,-253.5 1351.5,-247.5 1357.5,-241.5 1363.5,-241.5"/>
<text text-anchor="middle" x="1391.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">Quantity</text>
<polyline fill="none" stroke="#000000" points="1431.5,-241.5 1431.5,-277.5 "/>
<text text-anchor="middle" x="1442" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1452.5,-241.5 1452.5,-277.5 "/>
<text text-anchor="middle" x="1480" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">value</text>
<polyline fill="none" stroke="#000000" points="1507.5,-241.5 1507.5,-277.5 "/>
<text text-anchor="middle" x="1518" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Quantity&#45;&gt;Coding -->
<g id="edge3" class="edge">
<title>Quantity&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1438.1396,-241.3872C1434.6178,-215.1386 1424.8493,-166.1572 1399,-134 1390.2854,-123.1588 1379.5775,-113.5291 1368.0905,-105.0782"/>
<polygon fill="#000000" stroke="#000000" points="1369.8038,-102.005 1359.6058,-99.1325 1365.7866,-107.7376 1369.8038,-102.005"/>
<text text-anchor="middle" x="1424.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">unit</text>
</g>
<!-- Quantity&#45;&gt;Coding -->
<g id="edge5" class="edge">
<title>Quantity&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1423.3804,-241.4995C1404.7029,-221.8447 1372.9334,-190.0939 1342,-167 1329.2334,-157.4689 1321.6722,-160.8293 1311,-149 1301.8429,-138.85 1294.4359,-126.3138 1288.5701,-113.8261"/>
<polygon fill="#000000" stroke="#000000" points="1291.6185,-112.0643 1284.3815,-104.3264 1285.2135,-114.8885 1291.6185,-112.0643"/>
<text text-anchor="middle" x="1353" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">comparator</text>
</g>
<!-- Diagnosis -->
<g id="node9" class="node">
<title>Diagnosis</title>
<path fill="none" stroke="#000000" d="M179,-403.5C179,-403.5 523,-403.5 523,-403.5 529,-403.5 535,-409.5 535,-415.5 535,-415.5 535,-621.5 535,-621.5 535,-627.5 529,-633.5 523,-633.5 523,-633.5 179,-633.5 179,-633.5 173,-633.5 167,-627.5 167,-621.5 167,-621.5 167,-415.5 167,-415.5 167,-409.5 173,-403.5 179,-403.5"/>
<text text-anchor="middle" x="210" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">Diagnosis</text>
<polyline fill="none" stroke="#000000" points="253,-403.5 253,-633.5 "/>
<text text-anchor="middle" x="263.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="274,-403.5 274,-633.5 "/>
<text text-anchor="middle" x="394" y="-618.3" font-family="Times,serif" font-size="14.00" fill="#000000">age_at_diagnosis</text>
<polyline fill="none" stroke="#000000" points="274,-610.5 514,-610.5 "/>
<text text-anchor="middle" x="394" y="-595.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="274,-587.5 514,-587.5 "/>
<text text-anchor="middle" x="394" y="-572.3" font-family="Times,serif" font-size="14.00" fill="#000000">grade</text>
<polyline fill="none" stroke="#000000" points="274,-564.5 514,-564.5 "/>
<text text-anchor="middle" x="394" y="-549.3" font-family="Times,serif" font-size="14.00" fill="#000000">harmonized_primary_diagnosis</text>
<polyline fill="none" stroke="#000000" points="274,-541.5 514,-541.5 "/>
<text text-anchor="middle" x="394" y="-526.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="274,-518.5 514,-518.5 "/>
<text text-anchor="middle" x="394" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">morphology</text>
<polyline fill="none" stroke="#000000" points="274,-495.5 514,-495.5 "/>
<text text-anchor="middle" x="394" y="-480.3" font-family="Times,serif" font-size="14.00" fill="#000000">primary_diagnosis</text>
<polyline fill="none" stroke="#000000" points="274,-472.5 514,-472.5 "/>
<text text-anchor="middle" x="394" y="-457.3" font-family="Times,serif" font-size="14.00" fill="#000000">research_subject</text>
<polyline fill="none" stroke="#000000" points="274,-449.5 514,-449.5 "/>
<text text-anchor="middle" x="394" y="-434.3" font-family="Times,serif" font-size="14.00" fill="#000000">specimen</text>
<polyline fill="none" stroke="#000000" points="274,-426.5 514,-426.5 "/>
<text text-anchor="middle" x="394" y="-411.3" font-family="Times,serif" font-size="14.00" fill="#000000">stage</text>
<polyline fill="none" stroke="#000000" points="514,-403.5 514,-633.5 "/>
<text text-anchor="middle" x="524.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Diagnosis&#45;&gt;Identifier -->
<g id="edge13" class="edge">
<title>Diagnosis&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M475.2743,-403.1018C487.3273,-387.0144 498.0177,-369.8452 506,-352 525.3845,-308.6639 530.8529,-174.1075 532.3949,-103.0346"/>
<polygon fill="#000000" stroke="#000000" points="535.9025,-102.6797 532.6027,-92.6119 528.9039,-102.5401 535.9025,-102.6797"/>
<text text-anchor="middle" x="564.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Diagnosis&#45;&gt;Treatment -->
<g id="edge21" class="edge">
<title>Diagnosis&#45;&gt;Treatment</title>
<path fill="none" stroke="#000000" d="M343.4446,-403.3905C342.0108,-381.5466 340.5407,-359.1498 339.2003,-338.7275"/>
<polygon fill="#000000" stroke="#000000" points="342.6803,-338.307 338.5327,-328.5577 335.6953,-338.7655 342.6803,-338.307"/>
<text text-anchor="middle" x="378.5" y="-373.8" font-family="Times,serif" font-size="14.00" fill="#000000">treatment</text>
</g>
<!-- ExternalReference -->
<g id="node10" class="node">
<title>ExternalReference</title>
<path fill="none" stroke="#000000" d="M1471,-12C1471,-12 1753,-12 1753,-12 1759,-12 1765,-18 1765,-24 1765,-24 1765,-92 1765,-92 1765,-98 1759,-104 1753,-104 1753,-104 1471,-104 1471,-104 1465,-104 1459,-98 1459,-92 1459,-92 1459,-24 1459,-24 1459,-18 1465,-12 1471,-12"/>
<text text-anchor="middle" x="1534.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">ExternalReference</text>
<polyline fill="none" stroke="#000000" points="1610,-12 1610,-104 "/>
<text text-anchor="middle" x="1620.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1631,-12 1631,-104 "/>
<text text-anchor="middle" x="1687.5" y="-88.8" font-family="Times,serif" font-size="14.00" fill="#000000">reference_url</text>
<polyline fill="none" stroke="#000000" points="1631,-81 1744,-81 "/>
<text text-anchor="middle" x="1687.5" y="-65.8" font-family="Times,serif" font-size="14.00" fill="#000000">term_id</text>
<polyline fill="none" stroke="#000000" points="1631,-58 1744,-58 "/>
<text text-anchor="middle" x="1687.5" y="-42.8" font-family="Times,serif" font-size="14.00" fill="#000000">term_label</text>
<polyline fill="none" stroke="#000000" points="1631,-35 1744,-35 "/>
<text text-anchor="middle" x="1687.5" y="-19.8" font-family="Times,serif" font-size="14.00" fill="#000000">version</text>
<polyline fill="none" stroke="#000000" points="1744,-12 1744,-104 "/>
<text text-anchor="middle" x="1754.5" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- CodeableConcept -->
<g id="node11" class="node">
<title>CodeableConcept</title>
<path fill="none" stroke="#000000" d="M1115,-241.5C1115,-241.5 1321,-241.5 1321,-241.5 1327,-241.5 1333,-247.5 1333,-253.5 1333,-253.5 1333,-265.5 1333,-265.5 1333,-271.5 1327,-277.5 1321,-277.5 1321,-277.5 1115,-277.5 1115,-277.5 1109,-277.5 1103,-271.5 1103,-265.5 1103,-265.5 1103,-253.5 1103,-253.5 1103,-247.5 1109,-241.5 1115,-241.5"/>
<text text-anchor="middle" x="1174.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">CodeableConcept</text>
<polyline fill="none" stroke="#000000" points="1246,-241.5 1246,-277.5 "/>
<text text-anchor="middle" x="1256.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1267,-241.5 1267,-277.5 "/>
<text text-anchor="middle" x="1289.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">text</text>
<polyline fill="none" stroke="#000000" points="1312,-241.5 1312,-277.5 "/>
<text text-anchor="middle" x="1322.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- CodeableConcept&#45;&gt;Coding -->
<g id="edge16" class="edge">
<title>CodeableConcept&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1220.0081,-241.3704C1223,-216.7382 1229.4376,-171.4718 1240,-134 1241.8617,-127.3953 1244.0911,-120.5729 1246.4826,-113.8509"/>
<polygon fill="#000000" stroke="#000000" points="1249.8983,-114.7047 1250.0787,-104.1114 1243.3316,-112.2801 1249.8983,-114.7047"/>
<text text-anchor="middle" x="1264.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">coding</text>
</g>
<!-- Dataset -->
<g id="node12" class="node">
<title>Dataset</title>
<path fill="none" stroke="#000000" d="M1559,-179C1559,-179 1787,-179 1787,-179 1793,-179 1799,-185 1799,-191 1799,-191 1799,-328 1799,-328 1799,-334 1793,-340 1787,-340 1787,-340 1559,-340 1559,-340 1553,-340 1547,-334 1547,-328 1547,-328 1547,-191 1547,-191 1547,-185 1553,-179 1559,-179"/>
<text text-anchor="middle" x="1583" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">Dataset</text>
<polyline fill="none" stroke="#000000" points="1619,-179 1619,-340 "/>
<text text-anchor="middle" x="1629.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1640,-179 1640,-340 "/>
<text text-anchor="middle" x="1709" y="-324.8" font-family="Times,serif" font-size="14.00" fill="#000000">conformsTo</text>
<polyline fill="none" stroke="#000000" points="1640,-317 1778,-317 "/>
<text text-anchor="middle" x="1709" y="-301.8" font-family="Times,serif" font-size="14.00" fill="#000000">dct_title</text>
<polyline fill="none" stroke="#000000" points="1640,-294 1778,-294 "/>
<text text-anchor="middle" x="1709" y="-278.8" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="1640,-271 1778,-271 "/>
<text text-anchor="middle" x="1709" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="1640,-248 1778,-248 "/>
<text text-anchor="middle" x="1709" y="-232.8" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="1640,-225 1778,-225 "/>
<text text-anchor="middle" x="1709" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000">license</text>
<polyline fill="none" stroke="#000000" points="1640,-202 1778,-202 "/>
<text text-anchor="middle" x="1709" y="-186.8" font-family="Times,serif" font-size="14.00" fill="#000000">wasGeneratedBy</text>
<polyline fill="none" stroke="#000000" points="1778,-179 1778,-340 "/>
<text text-anchor="middle" x="1788.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Dataset&#45;&gt;Identifier -->
<g id="edge14" class="edge">
<title>Dataset&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M1558.8939,-178.8723C1551.5981,-174.6642 1544.2651,-170.6671 1537,-167 1517.2363,-157.024 1464.7669,-138.0405 1443,-134 1309.4448,-109.2087 967.0078,-130.9829 832,-116 778.7884,-110.0947 720.8965,-99.7878 670.3502,-89.4849"/>
<polygon fill="#000000" stroke="#000000" points="670.8426,-86.0129 660.3424,-87.4256 669.4318,-92.8693 670.8426,-86.0129"/>
<text text-anchor="middle" x="1524.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- Dataset&#45;&gt;ExternalReference -->
<g id="edge1" class="edge">
<title>Dataset&#45;&gt;ExternalReference</title>
<path fill="none" stroke="#000000" d="M1716.294,-178.6804C1719.3809,-163.4951 1718.9449,-148.0012 1712,-134 1707.9439,-125.8228 1702.5406,-118.2878 1696.3391,-111.4036"/>
<polygon fill="#000000" stroke="#000000" points="1698.8038,-108.9178 1689.3226,-104.1894 1693.7858,-113.7983 1698.8038,-108.9178"/>
<text text-anchor="middle" x="1790" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_use_restriction</text>
</g>
<!-- Dataset&#45;&gt;ExternalReference -->
<g id="edge7" class="edge">
<title>Dataset&#45;&gt;ExternalReference</title>
<path fill="none" stroke="#000000" d="M1583.5892,-178.9978C1576.9518,-169.5298 1571.2149,-159.4824 1567,-149 1562.2787,-137.2583 1563.7463,-124.9441 1568.3023,-113.3024"/>
<polygon fill="#000000" stroke="#000000" points="1571.5224,-114.6779 1572.559,-104.1339 1565.1734,-111.7301 1571.5224,-114.6779"/>
<text text-anchor="middle" x="1637.5" y="-137.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_use_limitation</text>
</g>
<!-- ResearchSubject&#45;&gt;Specimen -->
<g id="edge20" class="edge">
<title>ResearchSubject&#45;&gt;Specimen</title>
<path fill="none" stroke="#000000" d="M535.2668,-800.6701C499.4559,-867.9706 435.6284,-981.3367 368,-1070 365.3893,-1073.4227 362.7178,-1076.8524 359.995,-1080.2826"/>
<polygon fill="#000000" stroke="#000000" points="357.098,-1078.2998 353.5533,-1088.2841 362.5506,-1082.6895 357.098,-1078.2998"/>
<text text-anchor="middle" x="540.5" y="-940.8" font-family="Times,serif" font-size="14.00" fill="#000000">specimen</text>
</g>
<!-- ResearchSubject&#45;&gt;Identifier -->
<g id="edge15" class="edge">
<title>ResearchSubject&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M755.0703,-685.4611C775.946,-671.7685 794.4933,-654.8619 808,-634 863.7967,-547.8189 812.6523,-505.5612 808,-403 802.9203,-291.0155 792.9775,-251.2238 719,-167 693.6008,-138.0828 658.595,-114.8095 625.7986,-97.3118"/>
<polygon fill="#000000" stroke="#000000" points="627.1027,-94.0448 616.6167,-92.5298 623.8693,-100.2533 627.1027,-94.0448"/>
<text text-anchor="middle" x="840.5" y="-373.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- ResearchSubject&#45;&gt;File -->
<g id="edge2" class="edge">
<title>ResearchSubject&#45;&gt;File</title>
<path fill="none" stroke="#000000" d="M593.4411,-685.4772C599.9839,-672.2442 607.191,-657.6677 614.5391,-642.806"/>
<polygon fill="#000000" stroke="#000000" points="617.8331,-644.0406 619.1279,-633.5251 611.5582,-640.938 617.8331,-644.0406"/>
<text text-anchor="middle" x="619.5" y="-655.8" font-family="Times,serif" font-size="14.00" fill="#000000">file</text>
</g>
<!-- ResearchSubject&#45;&gt;Project -->
<g id="edge18" class="edge">
<title>ResearchSubject&#45;&gt;Project</title>
<path fill="none" stroke="#000000" d="M755.1084,-704.8879C793.5351,-693.9739 826.5974,-681.1502 841,-667 922.6389,-586.7919 949.3965,-454.0866 957.8102,-362.0029"/>
<polygon fill="#000000" stroke="#000000" points="961.3159,-362.085 958.681,-351.8231 954.3413,-361.4884 961.3159,-362.085"/>
<text text-anchor="middle" x="1020.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">associated_project</text>
</g>
<!-- ResearchSubject&#45;&gt;Diagnosis -->
<g id="edge19" class="edge">
<title>ResearchSubject&#45;&gt;Diagnosis</title>
<path fill="none" stroke="#000000" d="M510.1676,-685.4772C497.0775,-671.7448 482.6083,-656.5657 467.8873,-641.1224"/>
<polygon fill="#000000" stroke="#000000" points="470.0786,-638.3485 460.6453,-633.5251 465.0117,-643.1784 470.0786,-638.3485"/>
<text text-anchor="middle" x="524" y="-655.8" font-family="Times,serif" font-size="14.00" fill="#000000">diagnosis</text>
</g>
</g>
</svg>
</div>
