/* global L */
// 初始化地圖
const map = L.map("map", {
  center: [0, 0], // 中心座標
  crs: L.CRS.EPSG3857, // 使用 EPSG:3857 坐標系
  zoom: 2,
  worldCopyJump: true, // 無限滾動
  zoomSnap: 0.25, // 更小的縮放步長
  zoomDelta: 0.25, // 更小的縮放增量
  inertia: true, // 啟用慣性滾動
  inertiaDeceleration: 3000, // 慣性滾動減速
  inertiaMaxSpeed: 1500, // 慣性滾動最大速度
});

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  className: "grayscale",
}).addTo(map);


function addRoutesLayer(type, routecolor) {
  fetch("/api/routesmap_json").then((response) => response.json()).then((data) => {
    // console.log(data)
    const typeLayer = data[type]
    // console.log(commercialLayer)
    L.geoJSON(typeLayer, {
      style: {
        color: routecolor,
        weight: 3
      },
      onEachFeature: function (feature, layer) {
        if (feature.properties && feature.properties.start && feature.properties.end) {
          // 點擊顯示起點-終點
          layer.bindPopup(
            `<h3>${type}</h3>` +
            `<p>${feature.properties.start} - ${feature.properties.end}</p>`
          );
        }
      }
    }).addTo(map);
  });
}

addRoutesLayer("commercial", "#8FBC8F")
addRoutesLayer("cargo", "orange")

// fetch("/api/routesmap_json/")
//   .then((response) => response.json())
//   .then((data) => {
//     console.log(data);
//     const commercialLayer = L.layerGroup();
//     const cargoLayer = L.layerGroup();

//     const addGeoJsonLayer = (geojsonData, color, layerGroup) => {
//       L.geoJSON(geojsonData, {
//         noWrap: true,
//         style: {
//           color: color,
//           weight: 3,
//         },
//         coordsToLatLng: function (coords) {
//           return new L.LatLng(coords[1], coords[0]);
//         },
//         onEachFeature: function (feature, layer) {
//           if (
//             feature.properties &&
//             feature.properties.start &&
//             feature.properties.end
//           ) {
//             // 點擊顯示起點-終點
//             layer.bindPopup(
//               `<h3>${feature.properties.start} - ${feature.properties.end}</h3>`
//             );
//           }
//         },
//       }).addTo(layerGroup);
//     };
//     addGeoJsonLayer(data.commercial, "orange", commercialLayer);
//     addGeoJsonLayer(data.cargo, "lightgreen", cargoLayer);
//     commercialLayer.addTo(map);
//     cargoLayer.addTo(map);
//   });
