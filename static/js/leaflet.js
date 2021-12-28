var map = L.map('mapid', {
    // center: [22.604799,120.2976256],
    center: [25.056005105649245, 121.56811449676752],
    zoom: 16
  });
  
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
  
  
  
  var center = [25.056005105649245, 121.56811449676752];
  var marker = L.marker(center, {
    title: '跟 <a> 的 title 一樣', // 跟 <a> 的 title 一樣
    opacity: 1.0
  }).addTo(map);
  
  var circle = L.circle(
    center,   // 圓心座標
    50,                // 半徑（公尺）
    {
      color: 'red',      // 線條顏色
      fillColor: '#f03', // 填充顏色
      fillOpacity: 0.5   // 透明度
    }
  ).addTo(map);
  
  const center2 = [25.057005105649245, 121.56911449676752];
  const marker2 = L.marker(center2, {
    title: '跟 <a> 的 title 一樣', // 跟 <a> 的 title 一樣
    opacity: 1.0
  }).addTo(map);
  
  var circle = L.circle(
    center2,   // 圓心座標
    50,                // 半徑（公尺）
    {
      color: 'red',      // 線條顏色
      fillColor: '#f03', // 填充顏色
      fillOpacity: 0.5   // 透明度
    }
  ).addTo(map);

  