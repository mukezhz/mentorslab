export default function authHeader() {
  const access = localStorage.getItem("access_token")
  if (access) {
    return { Authorization: `Jwt ${access}` };
    // for Node.js Express back-end
    // return { "x-access-token": user.accessToken };
  }
  return {};
}
