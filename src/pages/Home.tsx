import React, { useState, ChangeEvent } from 'react'
import axios from 'axios'

interface IPredictData {
  Pregnancies: number
  Glucose: number
  BloodPressure: number
  SkinThickness: number
  Insulin: number
  BMI: number
  DiabetesPedigreeFunction: number
  Age: number
}

interface IResult {
  status?: string
  prediction?: number
  probability?: number
  error?: any
}

const Home: React.FC = () => {
  const [formData, setFormData] = useState<IPredictData>({
    Pregnancies: 0,
    Glucose: 0,
    BloodPressure: 0,
    SkinThickness: 0,
    Insulin: 0,
    BMI: 0,
    DiabetesPedigreeFunction: 0,
    Age: 0
  })

  const [result, setResult] = useState<IResult>({})

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData({ ...formData, [name]: parseFloat(value) })
  }

  const handleEvaluate = async () => {
    try {
      const res = await axios.post('http://localhost:5000/evaluate')
      setResult({ status: res.data.status })
    } catch (error: any) {
      setResult({ error: error.message })
    }
  }

  const handlePredict = async () => {
    try {
      const res = await axios.post('http://localhost:5000/predict', formData)
      setResult({
        prediction: res.data.prediction,
        probability: res.data.probability
      })
    } catch (error: any) {
      setResult({ error: error.message })
    }
  }

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      fontFamily: 'Arial, sans-serif',
      padding: '20px'
    }}>
      <h2 style={{ marginBottom: '10px' }}>Diabetes Detection</h2>
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: '10px',
        maxWidth: '400px',
        width: '100%',
        marginBottom: '20px'
      }}>
        <label>Pregnancies</label>
        <input
          type="number"
          name="Pregnancies"
          value={formData.Pregnancies}
          onChange={handleChange}
        />
        <label>Glucose</label>
        <input
          type="number"
          name="Glucose"
          value={formData.Glucose}
          onChange={handleChange}
        />
        <label>BloodPressure</label>
        <input
          type="number"
          name="BloodPressure"
          value={formData.BloodPressure}
          onChange={handleChange}
        />
        <label>SkinThickness</label>
        <input
          type="number"
          name="SkinThickness"
          value={formData.SkinThickness}
          onChange={handleChange}
        />
        <label>Insulin</label>
        <input
          type="number"
          name="Insulin"
          value={formData.Insulin}
          onChange={handleChange}
        />
        <label>BMI</label>
        <input
          type="number"
          step="0.1"
          name="BMI"
          value={formData.BMI}
          onChange={handleChange}
        />
        <label>DiabetesPedigreeFunction</label>
        <input
          type="number"
          step="0.01"
          name="DiabetesPedigreeFunction"
          value={formData.DiabetesPedigreeFunction}
          onChange={handleChange}
        />
        <label>Age</label>
        <input
          type="number"
          name="Age"
          value={formData.Age}
          onChange={handleChange}
        />
      </div>
      <div style={{ marginBottom: '20px' }}>
        <button
          onClick={handleEvaluate}
          style={{
            marginRight: '10px',
            padding: '8px 16px',
            cursor: 'pointer'
          }}
        >
          Evaluate
        </button>
        <button
          onClick={handlePredict}
          style={{
            padding: '8px 16px',
            cursor: 'pointer'
          }}
        >
          Predict
        </button>
      </div>
      <div style={{
        border: '1px solid #ccc',
        padding: '10px',
        width: '400px',
        minHeight: '60px'
      }}>
        {result.status && <p>Evaluation Status: {result.status}</p>}
        {result.prediction !== undefined && (
          <p>Prediction: {result.prediction}</p>
        )}
        {result.probability !== undefined && (
          <p>Probability: {result.probability}</p>
        )}
        {result.error && (
          <p style={{ color: 'red' }}>Error: {result.error}</p>
        )}
      </div>
    </div>
  )
}

export default Home
