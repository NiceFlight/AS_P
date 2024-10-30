const map = L.map('map').setView([25.0330, 121.5654], 10); // 台北市的中心座標
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);


// 加載外部 GeoJSON 文件
fetch('./static/js/town.geojson')
.then(response => response.json())
.then(townData => {
  L.geoJSON(townData, {
    style:function(feature){
        return{color: getColor(feature.properties.category)};
    },
    onEachFeature: function (feature, layer) {
      if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup(feature.properties.popupContent);
      }
    }
  }).addTo(map);
})
.catch(error => console.error('Error loading GeoJSON:', error));

// 設定顏色函數
function getColor(category) {
  switch (category) {
    // case 'landmark': return 'blue';
    // case 'other': return 'green';
    default: return 'orange';
  }
}