import { csrf_token } from "./csrf.js";


// 初始化地圖
const map = L.map("map", {
  center: [23.97565, 120.9738819],
  zoom: 7
}); // 台灣的中心座標

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

/* PHOTO2: 正射影像；EMAP5: 電子地圖；B50000、B10000: 地形圖；DDEM05: DEM */
// L.tileLayer("https://wmts.nlsc.gov.tw/wmts/EMAP5/default/EPSG:3857/{z}/{y}/{x}.png", {
//   attribution: '&copy;國土測繪中心 contributors',
// }).addTo(map);


// 顯示座標
/* global proj4 */
// 定義座標轉換參數
proj4.defs("EPSG:3826", "+proj=tmerc +lat_0=0 +lon_0=121 +k=0.9999 +x_0=250000 +y_0=0 +ellps=GRS80 +units=m +no_defs");
const coordsTWD97 = document.getElementById("coordsTWD97");
const coordsWGS84 = document.getElementById("coordsWGS84");
map.on("mousemove", function (e) {
  // 提取 lat lng
  const lat = e.latlng.lat.toFixed(6);
  const lng = e.latlng.lng.toFixed(6);
  // 座標轉換
  const twd97 = proj4("EPSG:4326", "EPSG:3826", [parseFloat(lng), parseFloat(lat)]);
  // console.log(twd97);
  // 顯示 TWD97 座標
  coordsTWD97.textContent = `X, Y：${twd97[0].toFixed(6)}, ${twd97[1].toFixed(6)}`;
  // // 顯示 WGS84 座標
  coordsWGS84.textContent = `Lat, Lng：${lat}, ${lng}`;
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
        const coordinates = data.coordinates;
        const filterData = data.filterData;

        // 清除geojsonLayer
        if (geojsonLayer) {
          map.removeLayer(geojsonLayer);
        }

        // 清除標記
        map.eachLayer(function (layer) {
          if (layer instanceof L.Marker) {
            map.removeLayer(layer);
          }
        });

        // 清空列表
        const locationList = document.getElementById("location-list");
        locationList.innerHTML = "";

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

        // 如果沒有座標資料，表格清空
        // console.log(coordinates);
        if (!coordinates || coordinates.length === 0) {
          locationList.textContent = "目前沒有資料。";
          return;
        }

        const table = document.createElement("table");
        table.style.borderCollapse = "collapse";
        table.style.width = "100%"

        let row;
        coordinates.forEach((location, index) => {
          var marker = L.marker([location.lat, location.lng]).addTo(map).bindPopup(`<h3>${location.name}</h3>`);

          marker.on("mouseover", function () {
            this.openPopup();
          });

          marker.on("mouseout", function () {
            this.closePopup();
          });

          if (index % 10 === 0) {
            row = document.createElement("tr");
            table.appendChild(row);
          }

          const cell = document.createElement("td");
          const listItem = document.createElement("li");
          const link = document.createElement("a");
          link.href = `https://www.google.com/maps/dir/?api=1&destination=${location.lat},${location.lng}`;
          link.target = "_blank";
          link.textContent = `${location.name}`;
          // listItem.textContent = `${location.name}`;
          listItem.appendChild(link);
          cell.appendChild(listItem);
          row.appendChild(cell);
        });
        locationList.appendChild(table);
      } else {
        console.error("error:", data.error);
      }
    })
    .catch((error) => console.error("Error:", error));
});
