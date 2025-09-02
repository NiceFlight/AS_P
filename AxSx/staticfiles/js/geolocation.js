/* global L */
document.addEventListener("DOMContentLoaded", () => {
  // 檢查瀏覽器是否支援 geolocation
  if (!("geolocation" in navigator)) {
    console.log("瀏覽器不支援 Geolocation");
    initMap(25.033, 121.5654); // fallback 台北 101
    return;
  } else {
    console.log("瀏覽器支援 Geolocation");
  }

  const options = {
    // 啟用高精度定位（例如使用 GPS），可能會耗費更多資源或時間
    enableHighAccuracy: true,
    // 設定定位操作的最大等待時間（毫秒），這裡是 5000 毫秒 = 5 秒
    timeout: 5000,
    // 設定可接受的快取位置資料的最大時間（毫秒），0 表示不使用快取，強制重新取得位置
    maximumAge: 0,
  };

  navigator.geolocation.getCurrentPosition(
    (position) => {
      const lat = position.coords.latitude;
      const lng = position.coords.longitude;
      console.log(`緯度：${lat}，經度：${lng}`);
      initMap(lat, lng);
    },
    (error) => {
      console.error(`錯誤：${error.message}`);
      initMap(25.033, 121.5654); // fallback 台北 101
    },
    options
  );
});
function initMap(lat, lng) {
  const map = L.map("map").setView([lat, lng], 13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "© OpenStreetMap contributors",
  }).addTo(map);
  L.marker([lat, lng]).addTo(map);
}
