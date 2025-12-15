// 從 document.cookie 找出名為 csrftoken 的值
export function csrf_token() {
  return document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    ?.split("=")[1];
}

// console.log(csrf_token());
// console.log(document.cookie);
