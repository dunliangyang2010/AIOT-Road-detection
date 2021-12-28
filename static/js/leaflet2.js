// // 另一種寫法
// var map = L.map('map', {
//     center: [25.056005105649245, 121.56811449676752],
//     zoom: 16
// });

// 建立 Leaflet 地圖
var map = L.map('map');

// 設定經緯度座標 new L.LatLng可直接以list[25.056005105649245, 121.56811449676752]取代
map.setView(new L.LatLng(25.033671, 121.564427), 10);

// 設定圖資來源
var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 18});
map.addLayer(osm);
