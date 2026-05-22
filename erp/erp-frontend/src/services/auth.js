import axios from "axios"

const api = axios.create({
  baseURL: "http://erp.local/api/v1"
})

export async function login(email, password) {

  const response = await api.post("/auth/login", {
    email,
    password
  })

  return response.data
}

export async function getMe(token) {

  const response = await api.get("/auth/me", {
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  return response.data
}