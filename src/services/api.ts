import axios from 'axios'

const apiClient = axios.create({
  baseURL: process.env.API_URL || 'http://localhost:5000',
  timeout: 10000
})

export async function trainModel() {
  const response = await apiClient.post('/train')
  return response.data
}

export async function evaluateModel() {
  const response = await apiClient.post('/evaluate')
  return response.data
}

export async function predictDiabetes(data: Record<string, any>) {
  const response = await apiClient.post('/predict', data)
  return response.data
}
