import { csrf_token } from "./csrf.js";


// 初始化地圖
const map = L.map("map").setView([23.97565, 120.9738819], 8); // 台灣的中心座標

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);


// 顯示座標
/* global proj4 */
// 定義座標轉換參數
proj4.defs("EPSG:3826", "+proj=tmerc +lat_0=0 +lon_0=121 +k=0.9999 +x_0=250000 +y_0=0 +ellps=GRS80 +units=m +no_defs");
const coordsDisplay = document.getElementById("coords");
map.on("mousemove", function (e) {
  // 提取 lat lng
  const lat = e.latlng.lat.toFixed(6);
  const lng = e.latlng.lng.toFixed(6);
  // 座標轉換
  const twd97 = proj4("EPSG:4326", "EPSG:3826", [parseFloat(lng), parseFloat(lat)]);
  // console.log(twd97);
  // 顯示在地圖上
  coordsDisplay.textContent = `X, Y：${twd97[0].toFixed(6)}, ${twd97[1].toFixed(6)}`;
});


var geojsonLayer = null;
const townSelect = document.getElementById("selectedTown");

document.getElementById("selectedTown").addEventListener("change", function () {
  var filterTown = townSelect.value.split("(")[1].substring(0, 3);
  // console.log(townSelect.value.slice(-4, -1))
  // 異步請求，將選擇的資料送到後端伺服器查詢
  fetch("api/views_AxSx/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Django template 渲染的變數{{ csrf_token }} 或從 document.cookie 找出名為csrftoken 的值
      "X-CSRFToken": window.csrfToken || csrf_token(),
    },
    body: JSON.stringify({ filterTown: filterTown }),
  })
    .then((response) => response.json()) // 後端伺服器回傳查詢結果並 Json 格式化
    .then((data) => {
      // 在地圖上標記
      if (data.status === "success") {
        var coordinates = data.coordinates;
        var filterData = data.filterData;

        // 清除geojsonLayer
        if (geojsonLayer) {
          map.removeLayer(geojsonLayer);
        }

        geojsonLayer = L.geoJSON(filterData, {
          style: function () {
            return {
              color: "#ff0000",
              weight: 3,
            };
          },
        }).addTo(map);

        // 更新邊界
        var bounds = geojsonLayer.getBounds();
        map.fitBounds(bounds);

        // 清除標記
        map.eachLayer(function (layer) {
          if (layer instanceof L.Marker) {
            map.removeLayer(layer);
          }
        });
        coordinates.forEach(function (coord) {
          var marker = L.marker([coord.lat, coord.lng]).addTo(map).bindPopup(`<h3>${coord.name}</h3>`);
          marker.on("mouseover", function () {
            this.openPopup();
          });
          marker.on("mouseout", function () {
            this.closePopup();
          });
          // 列出標記
          const locationList = document.getElementById("location-list");
          locationList.innerHTML = "";
          data.coordinates.forEach((location) => {
            const listItem = document.createElement("li");
            listItem.textContent = `${location.name}`;
            locationList.appendChild(listItem);
          });
        });
      } else {
        console.error("error:", data.error);
      }
    })
    .catch((error) => console.error("Error:", error));
});
