import React from 'react'

const About: React.FC = () => {
  return (
    <div style={{
      padding: '30px',
      fontFamily: 'Arial, sans-serif',
      textAlign: 'center'
    }}>
      <h2 style={{ fontSize: '2rem', marginBottom: '1rem' }}>About This Project</h2>
      <p style={{ fontSize: '1rem', maxWidth: '600px', margin: '0 auto' }}>
        This application is designed to help detect the risk of diabetes using predictive models.
        It integrates a Python backend for data processing, training, and inference, with a modern React
        frontend for an intuitive user experience. The project aims to bridge medical insights with
        practical software solutions, enhancing early detection and health management.
      </p>
    </div>
  )
}

export default About
