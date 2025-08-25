/* global L */
// 設定下拉選單
// const citySelect = document.getElementById("selectedCity");
// const townSelect = document.getElementById("selectedTown");

// TEST
// fetch("citytown/").then((response) => response.json()).then((data) => {
//   aaa = data
//   console.log(aaa)
// });

// 假設有一個 JSON 資料結構，包含縣市與鄉鎮的對應關係
// fetch("/static/js/city_town_ID.json")
//   .then((response) => response.json())
//   .then((data) => {
//     const cityTowns = data;
//     // console.log(cityTowns)

//     // 動態填充縣市選項
//     for (const city in cityTowns) {
//       // console.log(city);
//       const option = document.createElement("option");
//       option.value = city;
//       option.textContent = city;
//       citySelect.appendChild(option);
//     }

//     // 監聽縣市選項的變化
//     citySelect.addEventListener("change", () => {
//       const selectedCity = citySelect.value;
//       const towns = cityTowns[selectedCity];

//       // 清空鄉鎮選項
//       townSelect.innerHTML = '<option value="">請選擇鄉鎮</option>';

//       // 動態填充鄉鎮選項
//       towns.forEach((town) => {
//         const option = document.createElement("option");
//         option.value = town;
//         option.textContent = town;
//         townSelect.appendChild(option);
//       });
//       townSelect.disabled = false;
//     });
//   })
//   .catch((error) => console.error("Error:", error));

// 初始化地圖
const map = L.map("map").setView([23.97565, 120.9738819], 8); // 台灣的中心座標

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

export { map };

// 顯示座標
/* global proj4 */
// 定義座標轉換參數
// proj4.defs("EPSG:3826", "+proj=tmerc +lat_0=0 +lon_0=121 +k=0.9999 +x_0=250000 +y_0=0 +ellps=GRS80 +units=m +no_defs");
// const coordsDisplay = document.getElementById("coords");
// map.on("mousemove", function (e) {
//   // 提取 lat lng
//   const lat = e.latlng.lat.toFixed(6);
//   const lng = e.latlng.lng.toFixed(6);
//   // 座標轉換
//   const twd97 = proj4("EPSG:4326", "EPSG:3826", [parseFloat(lng), parseFloat(lat)]);
//   // console.log(twd97);
//   // 顯示在地圖上
//   coordsDisplay.textContent = `X, Y：${twd97[0].toFixed(6)}, ${twd97[1].toFixed(6)}`;
// });

// 從 document.cookie 找出名為 csrftoken 的值
// function csrf_token() {
//   return document.cookie
//     .split("; ")
//     .find((row) => row.startsWith("csrftoken="))
//     ?.split("=")[1];
// }
// // console.log(csrf_token());
// // console.log(document.cookie);

// var geojsonLayer = null;
// document.getElementById("selectedTown").addEventListener("change", function () {
//   var filterTown = townSelect.value.split("(")[1].substring(0, 3);
//   // console.log(townSelect.value.slice(-4, -1))
//   // 異步請求，將選擇的資料送到後端伺服器查詢
//   fetch("api/views_AxSx/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       // 以下二擇一
//       "X-CSRFToken": window.csrfToken, // Django template 渲染時注入的變數{{ csrf_token }}
//       // "X-CSRFToken": csrf_token(), // 從 document.cookie 找出名為 csrftoken 的值
//     },
//     body: JSON.stringify({ filterTown: filterTown }),
//   })
//     .then((response) => response.json()) // 後端伺服器回傳查詢結果並 Json 格式化
//     .then((data) => {
//       // 在地圖上標記
//       if (data.status === "success") {
//         var coordinates = data.coordinates;
//         var filterData = data.filterData;

//         // 清除geojsonLayer
//         if (geojsonLayer) {
//           map.removeLayer(geojsonLayer);
//         }

//         geojsonLayer = L.geoJSON(filterData, {
//           style: function () {
//             return {
//               color: "#ff0000",
//               weight: 3,
//             };
//           },
//         }).addTo(map);

//         // 更新邊界
//         var bounds = geojsonLayer.getBounds();
//         map.fitBounds(bounds);

//         // 清除標記
//         map.eachLayer(function (layer) {
//           if (layer instanceof L.Marker) {
//             map.removeLayer(layer);
//           }
//         });
//         coordinates.forEach(function (coord) {
//           var marker = L.marker([coord.lat, coord.lng]).addTo(map).bindPopup(`<h3>${coord.name}</h3>`);
//           marker.on("mouseover", function () {
//             this.openPopup();
//           });
//           marker.on("mouseout", function () {
//             this.closePopup();
//           });
//           // 列出標記
//           const locationList = document.getElementById("location-list");
//           locationList.innerHTML = "";
//           data.coordinates.forEach((location) => {
//             const listItem = document.createElement("li");
//             listItem.textContent = `${location.name}`;
//             locationList.appendChild(listItem);
//           });
//         });
//       } else {
//         console.error("error:", data.error);
//       }
//     })
//     .catch((error) => console.error("Error:", error));
// });
