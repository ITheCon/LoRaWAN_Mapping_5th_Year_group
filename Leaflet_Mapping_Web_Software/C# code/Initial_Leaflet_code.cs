﻿using System;
< link rel = "stylesheet" href = "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
   integrity = "sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
   crossorigin = "" />

# mapid { height: 180px; }

public class Map
{
	public Map()
	{
		var mymap = L.map('mapid').setView([51.505, -0.09], 13);
	}
}

 < div id = "mapid" ></ div >
 

 < !--Make sure you put this AFTER Leaflet's CSS -->
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
   integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
   crossorigin=""></script>