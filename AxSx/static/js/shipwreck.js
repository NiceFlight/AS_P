// 初始化地圖
const map = L.map("map", {
    center: [23.97565, 120.9738819],  // 中心座標
    crs: L.CRS.EPSG3857,
    zoom: 7,
    worldCopyJump: true,  // 無限滾動
    zoomSnap: 0.25, // 更小的縮放步長
    zoomDelta: 0.25, // 更小的縮放增量
    inertia: true, // 啟用慣性滾動
    inertiaDeceleration: 3000, // 慣性滾動減速
    inertiaMaxSpeed: 1500,  // 慣性滾動最大速度
});

// 添加底圖
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', className: 'grayscale'
}).addTo(map);
