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
<svg width="2145pt" height="878pt"
 viewBox="0.00 0.00 2145.00 878.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 874)">
<title>Perl</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-874 2141,-874 2141,4 -4,4"/>
<!-- Project -->
<g id="node1" class="node">
<title>Project</title>
<path fill="none" stroke="#000000" d="M12,-415C12,-415 236,-415 236,-415 242,-415 248,-421 248,-427 248,-427 248,-587 248,-587 248,-593 242,-599 236,-599 236,-599 12,-599 12,-599 6,-599 0,-593 0,-587 0,-587 0,-427 0,-427 0,-421 6,-415 12,-415"/>
<text text-anchor="middle" x="34" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">Project</text>
<polyline fill="none" stroke="#000000" points="68,-415 68,-599 "/>
<text text-anchor="middle" x="78.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="89,-415 89,-599 "/>
<text text-anchor="middle" x="158" y="-583.8" font-family="Times,serif" font-size="14.00" fill="#000000">dbgap_accession</text>
<polyline fill="none" stroke="#000000" points="89,-576 227,-576 "/>
<text text-anchor="middle" x="158" y="-560.8" font-family="Times,serif" font-size="14.00" fill="#000000">dct_title</text>
<polyline fill="none" stroke="#000000" points="89,-553 227,-553 "/>
<text text-anchor="middle" x="158" y="-537.8" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="89,-530 227,-530 "/>
<text text-anchor="middle" x="158" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">disease_site</text>
<polyline fill="none" stroke="#000000" points="89,-507 227,-507 "/>
<text text-anchor="middle" x="158" y="-491.8" font-family="Times,serif" font-size="14.00" fill="#000000">disease_type</text>
<polyline fill="none" stroke="#000000" points="89,-484 227,-484 "/>
<text text-anchor="middle" x="158" y="-468.8" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="89,-461 227,-461 "/>
<text text-anchor="middle" x="158" y="-445.8" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="89,-438 227,-438 "/>
<text text-anchor="middle" x="158" y="-422.8" font-family="Times,serif" font-size="14.00" fill="#000000">program</text>
<polyline fill="none" stroke="#000000" points="227,-415 227,-599 "/>
<text text-anchor="middle" x="237.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Study -->
<g id="node8" class="node">
<title>Study</title>
<path fill="none" stroke="#000000" d="M16.5,-156C16.5,-156 231.5,-156 231.5,-156 237.5,-156 243.5,-162 243.5,-168 243.5,-168 243.5,-259 243.5,-259 243.5,-265 237.5,-271 231.5,-271 231.5,-271 16.5,-271 16.5,-271 10.5,-271 4.5,-265 4.5,-259 4.5,-259 4.5,-168 4.5,-168 4.5,-162 10.5,-156 16.5,-156"/>
<text text-anchor="middle" x="34" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000">Study</text>
<polyline fill="none" stroke="#000000" points="63.5,-156 63.5,-271 "/>
<text text-anchor="middle" x="74" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="84.5,-156 84.5,-271 "/>
<text text-anchor="middle" x="153.5" y="-255.8" font-family="Times,serif" font-size="14.00" fill="#000000">dbgap_accession</text>
<polyline fill="none" stroke="#000000" points="84.5,-248 222.5,-248 "/>
<text text-anchor="middle" x="153.5" y="-232.8" font-family="Times,serif" font-size="14.00" fill="#000000">embargo_date</text>
<polyline fill="none" stroke="#000000" points="84.5,-225 222.5,-225 "/>
<text text-anchor="middle" x="153.5" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="84.5,-202 222.5,-202 "/>
<text text-anchor="middle" x="153.5" y="-186.8" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="84.5,-179 222.5,-179 "/>
<text text-anchor="middle" x="153.5" y="-163.8" font-family="Times,serif" font-size="14.00" fill="#000000">value</text>
<polyline fill="none" stroke="#000000" points="222.5,-156 222.5,-271 "/>
<text text-anchor="middle" x="233" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Project&#45;&gt;Study -->
<g id="edge13" class="edge">
<title>Project&#45;&gt;Study</title>
<path fill="none" stroke="#000000" d="M124,-414.94C124,-371.6378 124,-320.9219 124,-281.2112"/>
<polygon fill="#000000" stroke="#000000" points="127.5001,-281.1031 124,-271.1032 120.5001,-281.1032 127.5001,-281.1031"/>
<text text-anchor="middle" x="150" y="-327.8" font-family="Times,serif" font-size="14.00" fill="#000000">studies</text>
</g>
<!-- ResearchSubject -->
<g id="node2" class="node">
<title>ResearchSubject</title>
<path fill="none" stroke="#000000" d="M536,-731.5C536,-731.5 892,-731.5 892,-731.5 898,-731.5 904,-737.5 904,-743.5 904,-743.5 904,-834.5 904,-834.5 904,-840.5 898,-846.5 892,-846.5 892,-846.5 536,-846.5 536,-846.5 530,-846.5 524,-840.5 524,-834.5 524,-834.5 524,-743.5 524,-743.5 524,-737.5 530,-731.5 536,-731.5"/>
<text text-anchor="middle" x="593" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">ResearchSubject</text>
<polyline fill="none" stroke="#000000" points="662,-731.5 662,-846.5 "/>
<text text-anchor="middle" x="672.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="683,-731.5 683,-846.5 "/>
<text text-anchor="middle" x="783" y="-831.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="683,-823.5 883,-823.5 "/>
<text text-anchor="middle" x="783" y="-808.3" font-family="Times,serif" font-size="14.00" fill="#000000">harmonized_disease_type</text>
<polyline fill="none" stroke="#000000" points="683,-800.5 883,-800.5 "/>
<text text-anchor="middle" x="783" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="683,-777.5 883,-777.5 "/>
<text text-anchor="middle" x="783" y="-762.3" font-family="Times,serif" font-size="14.00" fill="#000000">primary_disease_site</text>
<polyline fill="none" stroke="#000000" points="683,-754.5 883,-754.5 "/>
<text text-anchor="middle" x="783" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000">primary_disease_type</text>
<polyline fill="none" stroke="#000000" points="883,-731.5 883,-846.5 "/>
<text text-anchor="middle" x="893.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- ResearchSubject&#45;&gt;Project -->
<g id="edge6" class="edge">
<title>ResearchSubject&#45;&gt;Project</title>
<path fill="none" stroke="#000000" d="M523.887,-759.1318C437.675,-739.4997 337.2983,-707.712 257,-657 235.5677,-643.4646 215.5654,-625.4897 197.914,-606.6971"/>
<polygon fill="#000000" stroke="#000000" points="200.3524,-604.1778 191.0112,-599.1786 195.196,-608.9119 200.3524,-604.1778"/>
<text text-anchor="middle" x="381.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">associated_project</text>
</g>
<!-- File -->
<g id="node6" class="node">
<title>File</title>
<path fill="none" stroke="#000000" d="M278,-392C278,-392 500,-392 500,-392 506,-392 512,-398 512,-404 512,-404 512,-610 512,-610 512,-616 506,-622 500,-622 500,-622 278,-622 278,-622 272,-622 266,-616 266,-610 266,-610 266,-404 266,-404 266,-398 272,-392 278,-392"/>
<text text-anchor="middle" x="288" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">File</text>
<polyline fill="none" stroke="#000000" points="310,-392 310,-622 "/>
<text text-anchor="middle" x="320.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="331,-392 331,-622 "/>
<text text-anchor="middle" x="411" y="-606.8" font-family="Times,serif" font-size="14.00" fill="#000000">byte_size</text>
<polyline fill="none" stroke="#000000" points="331,-599 491,-599 "/>
<text text-anchor="middle" x="411" y="-583.8" font-family="Times,serif" font-size="14.00" fill="#000000">checksum</text>
<polyline fill="none" stroke="#000000" points="331,-576 491,-576 "/>
<text text-anchor="middle" x="411" y="-560.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_category</text>
<polyline fill="none" stroke="#000000" points="331,-553 491,-553 "/>
<text text-anchor="middle" x="411" y="-537.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_type</text>
<polyline fill="none" stroke="#000000" points="331,-530 491,-530 "/>
<text text-anchor="middle" x="411" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="331,-507 491,-507 "/>
<text text-anchor="middle" x="411" y="-491.8" font-family="Times,serif" font-size="14.00" fill="#000000">file_format</text>
<polyline fill="none" stroke="#000000" points="331,-484 491,-484 "/>
<text text-anchor="middle" x="411" y="-468.8" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="331,-461 491,-461 "/>
<text text-anchor="middle" x="411" y="-445.8" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="331,-438 491,-438 "/>
<text text-anchor="middle" x="411" y="-422.8" font-family="Times,serif" font-size="14.00" fill="#000000">media_type</text>
<polyline fill="none" stroke="#000000" points="331,-415 491,-415 "/>
<text text-anchor="middle" x="411" y="-399.8" font-family="Times,serif" font-size="14.00" fill="#000000">reference_assembly</text>
<polyline fill="none" stroke="#000000" points="491,-392 491,-622 "/>
<text text-anchor="middle" x="501.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- ResearchSubject&#45;&gt;File -->
<g id="edge3" class="edge">
<title>ResearchSubject&#45;&gt;File</title>
<path fill="none" stroke="#000000" d="M619.714,-731.3347C587.1363,-709.671 551.2461,-683.7698 521,-657 511.2711,-648.3892 501.5635,-639.0874 492.0793,-629.481"/>
<polygon fill="#000000" stroke="#000000" points="494.3579,-626.8041 484.8736,-622.082 489.3431,-631.688 494.3579,-626.8041"/>
<text text-anchor="middle" x="572.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">file</text>
</g>
<!-- Specimen -->
<g id="node9" class="node">
<title>Specimen</title>
<path fill="none" stroke="#000000" d="M928,-357.5C928,-357.5 1248,-357.5 1248,-357.5 1254,-357.5 1260,-363.5 1260,-369.5 1260,-369.5 1260,-644.5 1260,-644.5 1260,-650.5 1254,-656.5 1248,-656.5 1248,-656.5 928,-656.5 928,-656.5 922,-656.5 916,-650.5 916,-644.5 916,-644.5 916,-369.5 916,-369.5 916,-363.5 922,-357.5 928,-357.5"/>
<text text-anchor="middle" x="959.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">Specimen</text>
<polyline fill="none" stroke="#000000" points="1003,-357.5 1003,-656.5 "/>
<text text-anchor="middle" x="1013.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1024,-357.5 1024,-656.5 "/>
<text text-anchor="middle" x="1131.5" y="-641.3" font-family="Times,serif" font-size="14.00" fill="#000000">age_at_collection</text>
<polyline fill="none" stroke="#000000" points="1024,-633.5 1239,-633.5 "/>
<text text-anchor="middle" x="1131.5" y="-618.3" font-family="Times,serif" font-size="14.00" fill="#000000">analyte_type</text>
<polyline fill="none" stroke="#000000" points="1024,-610.5 1239,-610.5 "/>
<text text-anchor="middle" x="1131.5" y="-595.3" font-family="Times,serif" font-size="14.00" fill="#000000">anatomical_site</text>
<polyline fill="none" stroke="#000000" points="1024,-587.5 1239,-587.5 "/>
<text text-anchor="middle" x="1131.5" y="-572.3" font-family="Times,serif" font-size="14.00" fill="#000000">cellular_composition</text>
<polyline fill="none" stroke="#000000" points="1024,-564.5 1239,-564.5 "/>
<text text-anchor="middle" x="1131.5" y="-549.3" font-family="Times,serif" font-size="14.00" fill="#000000">derived_from_specimen</text>
<polyline fill="none" stroke="#000000" points="1024,-541.5 1239,-541.5 "/>
<text text-anchor="middle" x="1131.5" y="-526.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="1024,-518.5 1239,-518.5 "/>
<text text-anchor="middle" x="1131.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">general_tissue_morphology</text>
<polyline fill="none" stroke="#000000" points="1024,-495.5 1239,-495.5 "/>
<text text-anchor="middle" x="1131.5" y="-480.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="1024,-472.5 1239,-472.5 "/>
<text text-anchor="middle" x="1131.5" y="-457.3" font-family="Times,serif" font-size="14.00" fill="#000000">matched_normal_flag</text>
<polyline fill="none" stroke="#000000" points="1024,-449.5 1239,-449.5 "/>
<text text-anchor="middle" x="1131.5" y="-434.3" font-family="Times,serif" font-size="14.00" fill="#000000">qualification_status_flag</text>
<polyline fill="none" stroke="#000000" points="1024,-426.5 1239,-426.5 "/>
<text text-anchor="middle" x="1131.5" y="-411.3" font-family="Times,serif" font-size="14.00" fill="#000000">source_material_type</text>
<polyline fill="none" stroke="#000000" points="1024,-403.5 1239,-403.5 "/>
<text text-anchor="middle" x="1131.5" y="-388.3" font-family="Times,serif" font-size="14.00" fill="#000000">specific_tissue_morphology</text>
<polyline fill="none" stroke="#000000" points="1024,-380.5 1239,-380.5 "/>
<text text-anchor="middle" x="1131.5" y="-365.3" font-family="Times,serif" font-size="14.00" fill="#000000">specimen_type</text>
<polyline fill="none" stroke="#000000" points="1239,-357.5 1239,-656.5 "/>
<text text-anchor="middle" x="1249.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- ResearchSubject&#45;&gt;Specimen -->
<g id="edge2" class="edge">
<title>ResearchSubject&#45;&gt;Specimen</title>
<path fill="none" stroke="#000000" d="M802.1504,-731.2065C835.4808,-708.7079 873.4496,-682.2909 907,-657 907.275,-656.7927 907.5501,-656.5852 907.8254,-656.3774"/>
<polygon fill="#000000" stroke="#000000" points="910.0023,-659.119 915.8468,-650.282 905.7671,-653.5456 910.0023,-659.119"/>
<text text-anchor="middle" x="916.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">specimen</text>
</g>
<!-- Diagnosis -->
<g id="node10" class="node">
<title>Diagnosis</title>
<path fill="none" stroke="#000000" d="M542,-392C542,-392 886,-392 886,-392 892,-392 898,-398 898,-404 898,-404 898,-610 898,-610 898,-616 892,-622 886,-622 886,-622 542,-622 542,-622 536,-622 530,-616 530,-610 530,-610 530,-404 530,-404 530,-398 536,-392 542,-392"/>
<text text-anchor="middle" x="573" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">Diagnosis</text>
<polyline fill="none" stroke="#000000" points="616,-392 616,-622 "/>
<text text-anchor="middle" x="626.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="637,-392 637,-622 "/>
<text text-anchor="middle" x="757" y="-606.8" font-family="Times,serif" font-size="14.00" fill="#000000">age_at_diagnosis</text>
<polyline fill="none" stroke="#000000" points="637,-599 877,-599 "/>
<text text-anchor="middle" x="757" y="-583.8" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="637,-576 877,-576 "/>
<text text-anchor="middle" x="757" y="-560.8" font-family="Times,serif" font-size="14.00" fill="#000000">grade</text>
<polyline fill="none" stroke="#000000" points="637,-553 877,-553 "/>
<text text-anchor="middle" x="757" y="-537.8" font-family="Times,serif" font-size="14.00" fill="#000000">harmonized_primary_diagnosis</text>
<polyline fill="none" stroke="#000000" points="637,-530 877,-530 "/>
<text text-anchor="middle" x="757" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="637,-507 877,-507 "/>
<text text-anchor="middle" x="757" y="-491.8" font-family="Times,serif" font-size="14.00" fill="#000000">morphology</text>
<polyline fill="none" stroke="#000000" points="637,-484 877,-484 "/>
<text text-anchor="middle" x="757" y="-468.8" font-family="Times,serif" font-size="14.00" fill="#000000">primary_diagnosis</text>
<polyline fill="none" stroke="#000000" points="637,-461 877,-461 "/>
<text text-anchor="middle" x="757" y="-445.8" font-family="Times,serif" font-size="14.00" fill="#000000">research_subject</text>
<polyline fill="none" stroke="#000000" points="637,-438 877,-438 "/>
<text text-anchor="middle" x="757" y="-422.8" font-family="Times,serif" font-size="14.00" fill="#000000">specimen</text>
<polyline fill="none" stroke="#000000" points="637,-415 877,-415 "/>
<text text-anchor="middle" x="757" y="-399.8" font-family="Times,serif" font-size="14.00" fill="#000000">stage</text>
<polyline fill="none" stroke="#000000" points="877,-392 877,-622 "/>
<text text-anchor="middle" x="887.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- ResearchSubject&#45;&gt;Diagnosis -->
<g id="edge5" class="edge">
<title>ResearchSubject&#45;&gt;Diagnosis</title>
<path fill="none" stroke="#000000" d="M714,-731.2526C714,-702.5804 714,-666.7524 714,-632.2054"/>
<polygon fill="#000000" stroke="#000000" points="717.5001,-632.0203 714,-622.0203 710.5001,-632.0204 717.5001,-632.0203"/>
<text text-anchor="middle" x="748" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">diagnosis</text>
</g>
<!-- Patient -->
<g id="node3" class="node">
<title>Patient</title>
<path fill="none" stroke="#000000" d="M1101,-121.5C1101,-121.5 1301,-121.5 1301,-121.5 1307,-121.5 1313,-127.5 1313,-133.5 1313,-133.5 1313,-293.5 1313,-293.5 1313,-299.5 1307,-305.5 1301,-305.5 1301,-305.5 1101,-305.5 1101,-305.5 1095,-305.5 1089,-299.5 1089,-293.5 1089,-293.5 1089,-133.5 1089,-133.5 1089,-127.5 1095,-121.5 1101,-121.5"/>
<text text-anchor="middle" x="1123" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000">Patient</text>
<polyline fill="none" stroke="#000000" points="1157,-121.5 1157,-305.5 "/>
<text text-anchor="middle" x="1167.5" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1178,-121.5 1178,-305.5 "/>
<text text-anchor="middle" x="1235" y="-290.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_to_birth</text>
<polyline fill="none" stroke="#000000" points="1178,-282.5 1292,-282.5 "/>
<text text-anchor="middle" x="1235" y="-267.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="1178,-259.5 1292,-259.5 "/>
<text text-anchor="middle" x="1235" y="-244.3" font-family="Times,serif" font-size="14.00" fill="#000000">ethnicity</text>
<polyline fill="none" stroke="#000000" points="1178,-236.5 1292,-236.5 "/>
<text text-anchor="middle" x="1235" y="-221.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="1178,-213.5 1292,-213.5 "/>
<text text-anchor="middle" x="1235" y="-198.3" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="1178,-190.5 1292,-190.5 "/>
<text text-anchor="middle" x="1235" y="-175.3" font-family="Times,serif" font-size="14.00" fill="#000000">race</text>
<polyline fill="none" stroke="#000000" points="1178,-167.5 1292,-167.5 "/>
<text text-anchor="middle" x="1235" y="-152.3" font-family="Times,serif" font-size="14.00" fill="#000000">sex</text>
<polyline fill="none" stroke="#000000" points="1178,-144.5 1292,-144.5 "/>
<text text-anchor="middle" x="1235" y="-129.3" font-family="Times,serif" font-size="14.00" fill="#000000">taxon</text>
<polyline fill="none" stroke="#000000" points="1292,-121.5 1292,-305.5 "/>
<text text-anchor="middle" x="1302.5" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Patient&#45;&gt;ResearchSubject -->
<g id="edge10" class="edge">
<title>Patient&#45;&gt;ResearchSubject</title>
<path fill="none" stroke="#000000" d="M1274.5341,-305.59C1277.4334,-311.627 1279.9655,-317.7833 1282,-324 1305.0337,-394.3832 1316.0869,-599.8408 1269,-657 1223.7225,-711.9627 1054.1959,-746.8277 914.2912,-766.8314"/>
<polygon fill="#000000" stroke="#000000" points="913.6838,-763.3824 904.2714,-768.2461 914.6625,-770.3136 913.6838,-763.3824"/>
<text text-anchor="middle" x="1379" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">research_subject_list</text>
</g>
<!-- Identifier -->
<g id="node4" class="node">
<title>Identifier</title>
<path fill="none" stroke="#000000" d="M629,-.5C629,-.5 799,-.5 799,-.5 805,-.5 811,-6.5 811,-12.5 811,-12.5 811,-57.5 811,-57.5 811,-63.5 805,-69.5 799,-69.5 799,-69.5 629,-69.5 629,-69.5 623,-69.5 617,-63.5 617,-57.5 617,-57.5 617,-12.5 617,-12.5 617,-6.5 623,-.5 629,-.5"/>
<text text-anchor="middle" x="659" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">Identifier</text>
<polyline fill="none" stroke="#000000" points="701,-.5 701,-69.5 "/>
<text text-anchor="middle" x="711.5" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="722,-.5 722,-69.5 "/>
<text text-anchor="middle" x="756" y="-54.3" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="722,-46.5 790,-46.5 "/>
<text text-anchor="middle" x="756" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">type</text>
<polyline fill="none" stroke="#000000" points="722,-23.5 790,-23.5 "/>
<text text-anchor="middle" x="756" y="-8.3" font-family="Times,serif" font-size="14.00" fill="#000000">value</text>
<polyline fill="none" stroke="#000000" points="790,-.5 790,-69.5 "/>
<text text-anchor="middle" x="800.5" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Quantity -->
<g id="node5" class="node">
<title>Quantity</title>
<path fill="none" stroke="#000000" d="M1374.5,-771C1374.5,-771 1527.5,-771 1527.5,-771 1533.5,-771 1539.5,-777 1539.5,-783 1539.5,-783 1539.5,-795 1539.5,-795 1539.5,-801 1533.5,-807 1527.5,-807 1527.5,-807 1374.5,-807 1374.5,-807 1368.5,-807 1362.5,-801 1362.5,-795 1362.5,-795 1362.5,-783 1362.5,-783 1362.5,-777 1368.5,-771 1374.5,-771"/>
<text text-anchor="middle" x="1402.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">Quantity</text>
<polyline fill="none" stroke="#000000" points="1442.5,-771 1442.5,-807 "/>
<text text-anchor="middle" x="1453" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1463.5,-771 1463.5,-807 "/>
<text text-anchor="middle" x="1491" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">value</text>
<polyline fill="none" stroke="#000000" points="1518.5,-771 1518.5,-807 "/>
<text text-anchor="middle" x="1529" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Coding -->
<g id="node11" class="node">
<title>Coding</title>
<path fill="none" stroke="#000000" d="M1480.5,-461C1480.5,-461 1635.5,-461 1635.5,-461 1641.5,-461 1647.5,-467 1647.5,-473 1647.5,-473 1647.5,-541 1647.5,-541 1647.5,-547 1641.5,-553 1635.5,-553 1635.5,-553 1480.5,-553 1480.5,-553 1474.5,-553 1468.5,-547 1468.5,-541 1468.5,-541 1468.5,-473 1468.5,-473 1468.5,-467 1474.5,-461 1480.5,-461"/>
<text text-anchor="middle" x="1502.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">Coding</text>
<polyline fill="none" stroke="#000000" points="1536.5,-461 1536.5,-553 "/>
<text text-anchor="middle" x="1547" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1557.5,-461 1557.5,-553 "/>
<text text-anchor="middle" x="1592" y="-537.8" font-family="Times,serif" font-size="14.00" fill="#000000">code</text>
<polyline fill="none" stroke="#000000" points="1557.5,-530 1626.5,-530 "/>
<text text-anchor="middle" x="1592" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">display</text>
<polyline fill="none" stroke="#000000" points="1557.5,-507 1626.5,-507 "/>
<text text-anchor="middle" x="1592" y="-491.8" font-family="Times,serif" font-size="14.00" fill="#000000">system</text>
<polyline fill="none" stroke="#000000" points="1557.5,-484 1626.5,-484 "/>
<text text-anchor="middle" x="1592" y="-468.8" font-family="Times,serif" font-size="14.00" fill="#000000">version</text>
<polyline fill="none" stroke="#000000" points="1626.5,-461 1626.5,-553 "/>
<text text-anchor="middle" x="1637" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Quantity&#45;&gt;Coding -->
<g id="edge4" class="edge">
<title>Quantity&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1448.1521,-770.7827C1445.2498,-747.8958 1442.4018,-707.6619 1452,-675 1464.1837,-633.5399 1489.8354,-592.4177 1512.8519,-561.2354"/>
<polygon fill="#000000" stroke="#000000" points="1515.7398,-563.2184 1518.9477,-553.1208 1510.1431,-559.014 1515.7398,-563.2184"/>
<text text-anchor="middle" x="1494" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">comparator</text>
</g>
<!-- Quantity&#45;&gt;Coding -->
<g id="edge9" class="edge">
<title>Quantity&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1472.4942,-770.9865C1492.5842,-752.7935 1521.5836,-722.7607 1536,-690 1553.5539,-650.1096 1558.6568,-600.8677 1559.5885,-563.515"/>
<polygon fill="#000000" stroke="#000000" points="1563.0912,-563.366 1559.7476,-553.3126 1556.092,-563.2568 1563.0912,-563.366"/>
<text text-anchor="middle" x="1556.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">unit</text>
</g>
<!-- ExternalReference -->
<g id="node7" class="node">
<title>ExternalReference</title>
<path fill="none" stroke="#000000" d="M1790,-461C1790,-461 2072,-461 2072,-461 2078,-461 2084,-467 2084,-473 2084,-473 2084,-541 2084,-541 2084,-547 2078,-553 2072,-553 2072,-553 1790,-553 1790,-553 1784,-553 1778,-547 1778,-541 1778,-541 1778,-473 1778,-473 1778,-467 1784,-461 1790,-461"/>
<text text-anchor="middle" x="1853.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000">ExternalReference</text>
<polyline fill="none" stroke="#000000" points="1929,-461 1929,-553 "/>
<text text-anchor="middle" x="1939.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1950,-461 1950,-553 "/>
<text text-anchor="middle" x="2006.5" y="-537.8" font-family="Times,serif" font-size="14.00" fill="#000000">reference_url</text>
<polyline fill="none" stroke="#000000" points="1950,-530 2063,-530 "/>
<text text-anchor="middle" x="2006.5" y="-514.8" font-family="Times,serif" font-size="14.00" fill="#000000">term_id</text>
<polyline fill="none" stroke="#000000" points="1950,-507 2063,-507 "/>
<text text-anchor="middle" x="2006.5" y="-491.8" font-family="Times,serif" font-size="14.00" fill="#000000">term_label</text>
<polyline fill="none" stroke="#000000" points="1950,-484 2063,-484 "/>
<text text-anchor="middle" x="2006.5" y="-468.8" font-family="Times,serif" font-size="14.00" fill="#000000">version</text>
<polyline fill="none" stroke="#000000" points="2063,-461 2063,-553 "/>
<text text-anchor="middle" x="2073.5" y="-503.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Specimen&#45;&gt;Patient -->
<g id="edge7" class="edge">
<title>Specimen&#45;&gt;Patient</title>
<path fill="none" stroke="#000000" d="M1114.0142,-357.19C1117.5322,-345.7923 1121.5086,-334.6076 1126,-324 1127.2882,-320.9575 1128.6654,-317.9114 1130.1177,-314.8715"/>
<polygon fill="#000000" stroke="#000000" points="1133.3234,-316.2868 1134.6858,-305.7799 1127.0686,-313.144 1133.3234,-316.2868"/>
<text text-anchor="middle" x="1204" y="-327.8" font-family="Times,serif" font-size="14.00" fill="#000000">derived_from_subject</text>
</g>
<!-- Treatment -->
<g id="node13" class="node">
<title>Treatment</title>
<path fill="none" stroke="#000000" d="M562.5,-144.5C562.5,-144.5 865.5,-144.5 865.5,-144.5 871.5,-144.5 877.5,-150.5 877.5,-156.5 877.5,-156.5 877.5,-270.5 877.5,-270.5 877.5,-276.5 871.5,-282.5 865.5,-282.5 865.5,-282.5 562.5,-282.5 562.5,-282.5 556.5,-282.5 550.5,-276.5 550.5,-270.5 550.5,-270.5 550.5,-156.5 550.5,-156.5 550.5,-150.5 556.5,-144.5 562.5,-144.5"/>
<text text-anchor="middle" x="596.5" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000">Treatment</text>
<polyline fill="none" stroke="#000000" points="642.5,-144.5 642.5,-282.5 "/>
<text text-anchor="middle" x="653" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="663.5,-144.5 663.5,-282.5 "/>
<text text-anchor="middle" x="760" y="-267.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_to_treatment_start</text>
<polyline fill="none" stroke="#000000" points="663.5,-259.5 856.5,-259.5 "/>
<text text-anchor="middle" x="760" y="-244.3" font-family="Times,serif" font-size="14.00" fill="#000000">days_treatment_end</text>
<polyline fill="none" stroke="#000000" points="663.5,-236.5 856.5,-236.5 "/>
<text text-anchor="middle" x="760" y="-221.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="663.5,-213.5 856.5,-213.5 "/>
<text text-anchor="middle" x="760" y="-198.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="663.5,-190.5 856.5,-190.5 "/>
<text text-anchor="middle" x="760" y="-175.3" font-family="Times,serif" font-size="14.00" fill="#000000">treatment_outcome</text>
<polyline fill="none" stroke="#000000" points="663.5,-167.5 856.5,-167.5 "/>
<text text-anchor="middle" x="760" y="-152.3" font-family="Times,serif" font-size="14.00" fill="#000000">treatment_type</text>
<polyline fill="none" stroke="#000000" points="856.5,-144.5 856.5,-282.5 "/>
<text text-anchor="middle" x="867" y="-209.8" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Diagnosis&#45;&gt;Treatment -->
<g id="edge1" class="edge">
<title>Diagnosis&#45;&gt;Treatment</title>
<path fill="none" stroke="#000000" d="M714,-391.8434C714,-358.6575 714,-323.2088 714,-292.7294"/>
<polygon fill="#000000" stroke="#000000" points="717.5001,-292.5938 714,-282.5938 710.5001,-292.5939 717.5001,-292.5938"/>
<text text-anchor="middle" x="750.5" y="-327.8" font-family="Times,serif" font-size="14.00" fill="#000000">treatment</text>
</g>
<!-- Dataset -->
<g id="node12" class="node">
<title>Dataset</title>
<path fill="none" stroke="#000000" d="M1817,-708.5C1817,-708.5 2045,-708.5 2045,-708.5 2051,-708.5 2057,-714.5 2057,-720.5 2057,-720.5 2057,-857.5 2057,-857.5 2057,-863.5 2051,-869.5 2045,-869.5 2045,-869.5 1817,-869.5 1817,-869.5 1811,-869.5 1805,-863.5 1805,-857.5 1805,-857.5 1805,-720.5 1805,-720.5 1805,-714.5 1811,-708.5 1817,-708.5"/>
<text text-anchor="middle" x="1841" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">Dataset</text>
<polyline fill="none" stroke="#000000" points="1877,-708.5 1877,-869.5 "/>
<text text-anchor="middle" x="1887.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1898,-708.5 1898,-869.5 "/>
<text text-anchor="middle" x="1967" y="-854.3" font-family="Times,serif" font-size="14.00" fill="#000000">conformsTo</text>
<polyline fill="none" stroke="#000000" points="1898,-846.5 2036,-846.5 "/>
<text text-anchor="middle" x="1967" y="-831.3" font-family="Times,serif" font-size="14.00" fill="#000000">dct_title</text>
<polyline fill="none" stroke="#000000" points="1898,-823.5 2036,-823.5 "/>
<text text-anchor="middle" x="1967" y="-808.3" font-family="Times,serif" font-size="14.00" fill="#000000">describedBy</text>
<polyline fill="none" stroke="#000000" points="1898,-800.5 2036,-800.5 "/>
<text text-anchor="middle" x="1967" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">id</text>
<polyline fill="none" stroke="#000000" points="1898,-777.5 2036,-777.5 "/>
<text text-anchor="middle" x="1967" y="-762.3" font-family="Times,serif" font-size="14.00" fill="#000000">label</text>
<polyline fill="none" stroke="#000000" points="1898,-754.5 2036,-754.5 "/>
<text text-anchor="middle" x="1967" y="-739.3" font-family="Times,serif" font-size="14.00" fill="#000000">license</text>
<polyline fill="none" stroke="#000000" points="1898,-731.5 2036,-731.5 "/>
<text text-anchor="middle" x="1967" y="-716.3" font-family="Times,serif" font-size="14.00" fill="#000000">wasGeneratedBy</text>
<polyline fill="none" stroke="#000000" points="2036,-708.5 2036,-869.5 "/>
<text text-anchor="middle" x="2046.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- Dataset&#45;&gt;ExternalReference -->
<g id="edge8" class="edge">
<title>Dataset&#45;&gt;ExternalReference</title>
<path fill="none" stroke="#000000" d="M1854.5771,-708.3578C1851.2361,-702.4037 1848.3212,-696.2667 1846,-690 1829.5412,-645.5643 1854.2082,-596.9938 1881.1349,-561.0647"/>
<polygon fill="#000000" stroke="#000000" points="1883.917,-563.1884 1887.2662,-553.1369 1878.3798,-558.9059 1883.917,-563.1884"/>
<text text-anchor="middle" x="1920" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_use_restriction</text>
</g>
<!-- Dataset&#45;&gt;ExternalReference -->
<g id="edge11" class="edge">
<title>Dataset&#45;&gt;ExternalReference</title>
<path fill="none" stroke="#000000" d="M1987.2337,-708.3431C1989.8993,-702.3055 1992.2058,-696.1614 1994,-690 2006.6442,-646.579 1988.5784,-598.2308 1968.5994,-562.139"/>
<polygon fill="#000000" stroke="#000000" points="1971.5064,-560.1723 1963.4964,-553.2376 1965.4336,-563.6538 1971.5064,-560.1723"/>
<text text-anchor="middle" x="2066.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">data_use_limitation</text>
</g>
<!-- Treatment&#45;&gt;Identifier -->
<g id="edge12" class="edge">
<title>Treatment&#45;&gt;Identifier</title>
<path fill="none" stroke="#000000" d="M714,-144.4872C714,-122.8658 714,-99.5716 714,-80.051"/>
<polygon fill="#000000" stroke="#000000" points="717.5001,-79.9233 714,-69.9233 710.5001,-79.9233 717.5001,-79.9233"/>
<text text-anchor="middle" x="747.5" y="-91.8" font-family="Times,serif" font-size="14.00" fill="#000000">identifier</text>
</g>
<!-- CodeableConcept -->
<g id="node14" class="node">
<title>CodeableConcept</title>
<path fill="none" stroke="#000000" d="M1569,-771C1569,-771 1775,-771 1775,-771 1781,-771 1787,-777 1787,-783 1787,-783 1787,-795 1787,-795 1787,-801 1781,-807 1775,-807 1775,-807 1569,-807 1569,-807 1563,-807 1557,-801 1557,-795 1557,-795 1557,-783 1557,-783 1557,-777 1563,-771 1569,-771"/>
<text text-anchor="middle" x="1628.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">CodeableConcept</text>
<polyline fill="none" stroke="#000000" points="1700,-771 1700,-807 "/>
<text text-anchor="middle" x="1710.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
<polyline fill="none" stroke="#000000" points="1721,-771 1721,-807 "/>
<text text-anchor="middle" x="1743.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000">text</text>
<polyline fill="none" stroke="#000000" points="1766,-771 1766,-807 "/>
<text text-anchor="middle" x="1776.5" y="-785.3" font-family="Times,serif" font-size="14.00" fill="#000000"> </text>
</g>
<!-- CodeableConcept&#45;&gt;Coding -->
<g id="edge14" class="edge">
<title>CodeableConcept&#45;&gt;Coding</title>
<path fill="none" stroke="#000000" d="M1664.6954,-770.9306C1648.0315,-729.7094 1606.6406,-627.3215 1580.5849,-562.8679"/>
<polygon fill="#000000" stroke="#000000" points="1583.6917,-561.2144 1576.6989,-553.2551 1577.2019,-563.838 1583.6917,-561.2144"/>
<text text-anchor="middle" x="1656.5" y="-678.8" font-family="Times,serif" font-size="14.00" fill="#000000">coding</text>
</g>
</g>
</svg>
</div>