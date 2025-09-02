import { map } from "./map.js";

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
